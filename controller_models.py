from app import db


class Controller(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    resources = db.relationship('Resource', backref='controller', lazy=True)


    def __repr__(self):
        return '<Privilege %r>' % self.nome

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

