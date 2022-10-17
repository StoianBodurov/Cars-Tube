from sqlalchemy import func

from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
