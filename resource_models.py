from argparse import Action
from enum import unique
from app import db


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action_id = db.Column(db.Integer, db.ForeignKey("action.id"), nullable=False)
    controller_id = db.Column(db.Integer, db.ForeignKey("controller.id"), nullable=False)
    privileges = db.relationship("Privilege", backref="resource")

    
    def __repr__(self):
        return '<Resource %r>' % self.id

    def to_dict(self):
        return {
            "id": self.id,
            "action_id": self.action_id,
            "controller_id": self.controller_id
        }