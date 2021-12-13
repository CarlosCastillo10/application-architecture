from src import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    email = db.Column(db.String(45))
    courses = db.relationship("Course", secondary="course_student", backref=db.backref('students', lazy='dynamic'), lazy='dynamic')

    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email
        }
