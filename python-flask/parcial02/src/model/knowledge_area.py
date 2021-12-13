from src import db


class KnowledgeArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    faculties = db.relationship("Faculty", backref="knowledge_area")

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
