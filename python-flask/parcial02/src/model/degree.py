from src import db


class Degree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    courses = db.relationship("Course", backref="degree")

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
