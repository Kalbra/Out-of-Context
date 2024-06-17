import random

from api.app import db, app
from api.models.teacher import Teacher
from api.models.quote import Quote
from faker import Faker
import os

os.chdir("../")


fake = Faker()


with app.app_context():
    db.drop_all()

    db.create_all()

    for i in range(20):
        db.session.add(Teacher(name=fake.name()))

    db.session.commit()

    for i in range(200):
        db.session.add(Quote(
            teacher_id=random.randint(1, 20),
            quote="".join(fake.sentences(3)),
            votes=random.randint(-200, 200)
        ))

    db.session.commit()
