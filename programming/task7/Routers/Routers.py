from flask import abort
from ..Model.CreditModel import Card
from ..app import db
from ..app import app
from flask import request, jsonify
from ..Model.CardException import *
from sqlalchemy import desc, cast


@app.get("/cards")
def get_cards():
    args = request.args
    sort_by = args.get('sort_by')
    limit = args.get('limit', type=int)
    offset = args.get('offset', type=int)
    sort_type = args.get('sort_type', default="desc")
    s = args.get('s')
    attribute = ["id", "bank", "card_number", "date_of_issue", "date_of_expire", "cvc", "owner_name"]
    cards = Card.query
    count = cards.count()
    if s:
        search_field = s.lower()
        field = Card.bank.like('%' + search_field + '%')
        for col in attribute:
            field |= cast(getattr(Card, col), db.String).ilike(f"%{search_field}%")
            print(field)
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
def get_card(card_id):
    card = Card.query.filter_by(id=card_id).first()
    if card is None:
        ex = CardException("No users found")
        return jsonify(ex.to_json()), 404
    return jsonify(card.to_json()), 200


@app.post("/cards")
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
        card = Card(bank, card_number, date_of_issue, date_of_expire, cvc, owner_name)
        if Card.query.filter_by(card_number=card.card_number).first():
            ex = CardException("Credit card already in use")
            return jsonify(ex.to_json()), 404
        db.session.add(card)
        db.session.commit()
    except Exception as ex:
        exception = CardException(str(ex))
        exception.add_ex("Wrong request params")
        db.session.rollback()
        return jsonify(exception.to_json()), 400
    return jsonify(card.to_json()), 201


@app.put('/cards/<int:id>')
def update_book(id):
    if not request.json:
        abort(400)
    card = Card.query.get(id)
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


@app.delete("/cards/<int:isbn>")
def delete_book(isbn):
    card = Card.query.get(isbn)
    if card is None:
        exception = CardException("Id in params doesn't exists")
        return jsonify(exception.to_json()), 404
    db.session.delete(card)
    db.session.commit()
    return jsonify({'result': True}), 200
