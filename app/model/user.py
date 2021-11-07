from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime,index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,index=True, default=datetime.utcnow,onupdate=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)