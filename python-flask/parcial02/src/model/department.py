from src import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    degrees = db.relationship("Degree", backref="department")

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
