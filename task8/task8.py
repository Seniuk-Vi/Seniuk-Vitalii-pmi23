from Routers.Routers import *
from flask_migrate import Migrate

if __name__ == '__main__':
    with app.app_context():
        # migrate = Migrate(app, db)
        db.drop_all()
        db.session.commit()
        db.create_all()
        h_password = generate_password_hash('Password', 'sha256')
        user_1 = UserModel(surname='surname', name='user',
                           password=h_password, admin=False, email='email1@lnu.ua')
        user_2 = UserModel(surname='surname', name='admin',
                           password=h_password, admin=True, email='email2@lnu.ua')
        card_1 = Card("privatbank",
                      "1234 1234 1234 1234",
                      "2020-01-01",
                      "2025-01-01",
                      123,
                      "Bob", 1)
        card_2 = Card("monobank",
                      "3212 1234 1234 1234",
                      "2020-01-01",
                      "2025-01-01",
                      123,
                      "Tom", 2)

        db.session.add(user_1)
        db.session.add(user_2)
        db.session.add(card_1)
        db.session.add(card_2)

        db.session.commit()
        app.run(debug=True)
