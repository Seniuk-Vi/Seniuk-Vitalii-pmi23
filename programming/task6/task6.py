from Seniuk.programming.task6.Routers.Routers import *
from init_db import *
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
        app.run(debug=True)
