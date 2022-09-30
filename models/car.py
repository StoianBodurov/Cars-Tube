from db import db


class CarModel(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String)
    year = db.Column(db.Date, nullable=False)
    image = db.Column(db.String(250))
    price = db.Column(db.Float, nullable=False)
