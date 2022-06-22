import email
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id
    
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "role_id": self.role_id
        }
