from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    datetime = db.Column(db.DateTime(), default=datetime.utcnow)


class DrugDB(db.Model):
    __tablename__ = 'drugs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    route = db.Column(db.String(64))
    dose = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    dispensed = db.Column(db.String(64))
    brandname = db.Column(db.String(64))
    status = db.Column(db.String(64))
    date = db.Column(db.DateTime(), default=datetime.utcnow)

class Premise(db.Model):
    __tablename__ = 'premise'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(120))
