from src import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    degree_id = db.Column(db.Integer, db.ForeignKey('degree.id'))

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
