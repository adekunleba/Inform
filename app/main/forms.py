from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SelectField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email


class Register(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class PremiseForm(FlaskForm):
    name = StringField('Premise Name', validators=[DataRequired(), Length(1, 64)])
    state = StringField('State', validators=[DataRequired()])
    town = StringField('Town', validators=[DataRequired()])
    lga = StringField('Local', validators=[DataRequired()])
    submit = SubmitField('Register')


class PatientForm(FlaskForm):
    patientName = StringField('Patient Name', validators=[DataRequired(), Length(1, 64)])
    patientID = IntegerField('PatientID')
    patientAge = StringField('Patient Age')
    patientState = StringField('State')
    patientLGA = StringField('LGA')
    submit = SubmitField('Add Patient')


class Drug(FlaskForm):
    drugName = StringField('Drug Name', validators=[DataRequired(), Length(1, 64)])
    drugRoute = StringField('Route of Administration', validators=[DataRequired()])
    drugDose = IntegerField('Drug Dosage', validators=[DataRequired()])
    drugStrenght = IntegerField('Dosage Available', validators=[DataRequired()])
    drugDuration = StringField('Duration of Use', validators=[DataRequired()])
    submit = SubmitField('Dispensed')


# class GroupedForm(FlaskForm):
#     """A form for one or more addresses"""
#     drugs = FieldList(FormField(Drug), max_entries=3)
