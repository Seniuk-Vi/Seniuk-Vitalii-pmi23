from flask import abort
from Seniuk.task8.Model.CreditModel import Card
from Seniuk.task8.app import db
from Seniuk.task8.app import app
from flask import request, jsonify, make_response, session
from Seniuk.task8.Model.CardException import *
from Seniuk.task8.Model.UserException import *
from Seniuk.task8.Model.UserModel import *
from Seniuk.task8.Model.TokenBlackList import *
from sqlalchemy import desc, cast, func
from flasgger import swag_from
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from functools import wraps
import jwt
from dotenv import load_dotenv
import datetime


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            exception = UserException("A valid token is missing")
            return jsonify(exception.to_json()), 401
        if TokenBlackList.query.filter_by(token=token).first():  # check if token isn't in black list
            exception = UserException("Login first")
            exception.add_ex('Token is invalid')
            return jsonify(exception.to_json()), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = UserModel.query.filter_by(id=data['id']).first()
        except Exception as ex:
            exception = UserException(str(ex))
            exception.add_ex("Token is invalid")
            return jsonify(exception.to_json()), 401

        return f(*args, **kwargs)

    return decorator


def admin_only(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers['x-access-tokens']
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            if 2 != data['id']:
                exception = UserException("You don't have permission")
                return jsonify(exception.to_json()), 403
        except Exception as ex:
            exception = UserException(str(ex))
            exception.add_ex("Token is invalid")
            return jsonify(exception.to_json()), 401
        return f(*args, **kwargs)

    return decorator


@app.post('/register')
@swag_from('../signup.yml')
def signup_user():
    if not request.json:
        exception = CardException("Wrong request params")
        return jsonify(exception.to_json()), 404
    try:
        data = request.get_json()
        # check password
        if not Validator.validate_with_regex(CreditCardRegex.password_regex, data['password']) or len(
                data['password']) < 8:
            raise AttributeError("Password is too weak (minimum 1 upper and minimum 1 lower and 8 characters)!!!")
        # check email
        user = UserModel.query.filter_by(email=data['email']).first()
        if user:
            raise AttributeError("Email already in use")

        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = UserModel(surname=data['surname'], name=data['name'],
                             password=hashed_password, admin=False, email=data['email'])
        db.session.add(new_user)
        db.session.commit()
    except Exception as ex:
        exception = CardException(str(ex))
        exception.add_ex("Wrong request params")
        db.session.rollback()
        return jsonify(exception.to_json()), 404
    return jsonify(new_user.to_json()), 201


@app.post('/login')
@swag_from('../login.yml')
def login_user():
    auth = request.form
    if not auth or not auth.get('email') or not auth.get('password'):
        exception = UserException("Could not verify")
        exception.add_ex('Email and password required')
        return jsonify(exception.to_json()), 404

    user = UserModel.query.filter_by(email=auth.get('email')).first()
    if not user:
        exception = UserException("Could not verify")
        exception.add_ex('User does not exist')
        return jsonify(exception.to_json()), 404
    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode(
            {'id': user.id, 'admin': user.admin, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
            app.config['SECRET_KEY'], "HS256")
        if TokenBlackList.query.filter_by(token=token).first():  # check if token isn't in black list
            exception = UserException("Could not login")
            exception.add_ex('Token in black list')
            return jsonify(exception.to_json()), 401
        return jsonify({'token': token}), 200
    exception = UserException("Could not verify")
    exception.add_ex('Email or password is wrong')
    return jsonify(exception.to_json()), 404


@app.post('/logout')
@swag_from('../logout.yml')
@token_required
def logout():
    token = request.headers['x-access-tokens']
    ban_token = TokenBlackList(token=token)
    db.session.add(ban_token)
    db.session.commit()
    return jsonify({"message": "Successfully logout"}), 200


@app.get("/cards")
@swag_from('../get_cards.yml')
@token_required
def get_cards():
    args = request.args
    sort_by = args.get('sort_by')
    limit = args.get('limit', type=int)
    offset = args.get('offset', type=int)
    sort_type = args.get('sort_type', default="desc")
    s = args.get('s')
    cards = Card.query
    count = cards.count()
    attribute = ["id", "bank", "card_number", "date_of_issue", "date_of_expire", "cvc", "owner_name"]
    if s:
        search_field = s.lower()
        field = Card.bank.like('%' + search_field + '%')
        for col in attribute:
            field |= cast(getattr(Card, col), db.String).ilike(f"%{search_field}%")
        cards = cards.filter(field)
    if sort_by:
        if sort_by not in Card.__dict__.keys():
            ex = CardException("Not appropriate attribute to sort")
            return jsonify(ex.to_json()), 400
        elif sort_type == "desc":
            cards = cards.order_by(desc(sort_by))
        else:
            cards = cards.order_by(sort_by)
    if offset is not None and limit is not None:
        cards = cards.offset(offset * limit).limit(limit).all()
    return jsonify({"Cards": [card.to_json() for card in cards], "Count": count}), 200


@app.get("/cards/<int:card_id>")
@swag_from('../get_card.yml')
@token_required
def get_card(card_id):
    card = Card.query.filter_by(id=card_id).first()
    if card is None:
        ex = CardException("No card found")
        return jsonify(ex.to_json()), 404
    return jsonify(card.to_json()), 200


@app.get("/users")
@swag_from('../get_users.yml')
def get_users():
    users = UserModel.query
   # return jsonify({"User":users.to_json()}), 200
    return jsonify({"Users": [user.to_json() for user in users]}), 200


@app.post("/cards")
@swag_from('../create_card.yml')
@token_required
@admin_only
def create_card():
    if not request.json:
        abort(404)
    try:
        bank = request.json['bank']
        card_number = request.json['card_number']
        date_of_issue = request.json['date_of_issue']
        date_of_expire = request.json['date_of_expire']
        cvc = request.json['cvc']
        owner_name = request.json['owner_name']
        user_id = request.json['user_id']
        card = Card(bank, card_number, date_of_issue, date_of_expire, cvc, owner_name, user_id)
        # check if user exists and have less than 5 cards
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            ex = CardException("User doesn't exists")
            return jsonify(ex.to_json()), 404
        if db.session.query(UserModel.id, func.count('*').label("count")).filter_by(id=user_id).join(Card).group_by(
                UserModel).all().pop()[1] > 4:
            ex = CardException("User already have 5 cards")
            return jsonify(ex.to_json()), 404
        # check if card is unique
        if Card.query.filter_by(card_number=card.card_number).first():
            ex = CardException("Credit card already in use")
            return jsonify(ex.to_json()), 404
        db.session.add(card)
        db.session.commit()

    except Exception as ex:
        exception = CardException("Wrong request params")
        exception.add_ex(str(ex))
        db.session.rollback()
        return jsonify(exception.to_json()), 400
    return jsonify(card.to_json()), 201


@app.put('/cards/<int:card_id>')
@swag_from('../update_card.yml')
@token_required
@admin_only
def update_card(card_id):
    if not request.json:
        abort(400)
    card = Card.query.get(card_id)
    if card is None:
        exception = CardException("Id in params doesn't exists")
        return jsonify(exception.to_json()), 404
    try:
        card.bank = request.json.get('bank', card.bank)
        card.card_number = request.json.get('card_number', card.card_number)
        card.date_of_issue = request.json.get('date_of_issue', card.date_of_issue)
        card.date_of_expire = request.json.get('date_of_expire', card.date_of_expire)
        card.owner_name = request.json.get('owner_name', card.owner_name)
        card.cvc = request.json.get('cvc', card.cvc)
        db.session.commit()
    except Exception as ex:
        exception = CardException(str(ex))
        exception.add_ex("Wrong update request params")
        db.session.rollback()
        return jsonify(exception.to_json()), 400

    return jsonify(card.to_json()), 200


@app.delete("/cards/<int:card_id>")
@swag_from('../delete_card.yml')
@token_required
@admin_only
def delete_card(card_id):
    card = Card.query.get(card_id)
    if card is None:
        exception = CardException("Id in params doesn't exists")
        return jsonify(exception.to_json()), 404
    db.session.delete(card)
    db.session.commit()
    return jsonify({'result': True}), 200
