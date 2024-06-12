from api.app import db, app
from api.models.teacher import Teacher
from faker import Faker

fake = Faker()

with app.app_context():

    db.create_all()

    for i in range(20):
        db.session.add(Teacher(name=fake.name()))

    db.session.commit()



