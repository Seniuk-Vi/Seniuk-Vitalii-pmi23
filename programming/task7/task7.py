from Seniuk.programming.task7.Routers.Routers import *
from flask_migrate import Migrate

if __name__ == '__main__':

    with app.app_context():
       # migrate = Migrate(app, db)
        db.drop_all()
        db.session.commit()
        db.create_all()
        card_1 = Card("privatbank",
                      "1234 1234 1234 1234",
                      "2020-01-01",
                      "2025-01-01",
                      123,
                      "Bob")
        card_2 = Card("monobank",
                      "3212 1234 1234 1234",
                      "2020-01-01",
                      "2025-01-01",
                      123,
                      "Tom")
        db.session.add(card_1)
        db.session.add(card_2)
        db.session.commit()
        app.run(debug=True)
