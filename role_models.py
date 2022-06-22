from enum import unique
from app import db


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    users = db.relationship('User', backref='role')
    privileges = db.relationship('Privilege', backref='role')
    
    
    def __repr__(self):
        return '<Role %r>' % self.nome

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

