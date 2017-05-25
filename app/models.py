from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    datetime = db.Column(db.DateTime(), default=datetime.utcnow)
    premises = db.relationship('Premise', backref='users', lazy='dynamic')

    @property
    def password(self, password):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


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
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    premise_id = db.Column(db.Integer, db.ForeignKey('premise.id'))


class Premise(db.Model):
    __tablename__ = 'premise'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    state = db.Column(db.String(120))
    lga = db.Column(db.String(120))
    town = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    patients = db.relationship('Patient', backref='patients', lazy='dynamic')


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    state = db.Column(db.String(64))
    lga = db.Column(db.String(64))
    age = db.Column(db.String(64))
    premise_id = db.Column(db.Integer, db.ForeignKey('premise.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    drugs_rel = db.relationship('DrugDB', backref='drugs_tab', lazy='dynamic')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
