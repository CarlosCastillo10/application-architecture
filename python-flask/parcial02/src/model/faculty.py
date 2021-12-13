from src import db


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    knowledge_area_id = db.Column(db.Integer, db.ForeignKey('knowledge_area.id'))
    departments = db.relationship("Department", backref="faculty")

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
