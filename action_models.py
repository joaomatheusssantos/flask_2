import resource
from app import db


class Action(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    resources = db.relationship("Resource", backref='action', lazy=True)


    def __repr__(self):
        return '<Action %r>' % self.nome

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

