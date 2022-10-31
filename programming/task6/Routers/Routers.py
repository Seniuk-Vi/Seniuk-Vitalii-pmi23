from flask import abort
from ..Model.CreditModel import Card
from ..app import db
from ..app import app
from flask import request, jsonify
from ..Model.CardException import *


@app.get("/cards")
def get_cards():
    cards = Card.query.all()
    return jsonify([card.to_json() for card in cards])


@app.get("/cards/<int:card_id>")
def get_card(card_id):
    card = Card.query.filter_by(id=card_id).first()
    if card is None:
        card = CardException("No users found")
    return jsonify(card.to_json()), 200


@app.post("/cards")
def create_card():
    if not request.json:
        abort(400)
    try:
        bank = request.json['bank']
        card_number = request.json['card_number']
        date_of_issue = request.json['date_of_issue']
        date_of_expire = request.json['date_of_expire']
        cvc = request.json['cvc']
        owner_name = request.json['owner_name']
        card = Card(bank, card_number, date_of_issue, date_of_expire, cvc, owner_name)
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
        abort(404)
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
        exception.add_ex("Wrong request params")
        db.session.rollback()
        return jsonify(exception.to_json()), 400

    return jsonify(card.to_json()), 202


@app.delete("/cards/<int:isbn>")
def delete_book(isbn):
    card = Card.query.get(isbn)
    if card is None:
        abort(404)
    db.session.delete(card)
    db.session.commit()
    return jsonify({'result': True})
