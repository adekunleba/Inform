from app import db
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class PremiseForm(FlaskForm):
    name = StringField('Premise Name', validators=[DataRequired(), Length(1, 64)])
    address = StringField('Address', validators=[DataRequired()])


class Drug(FlaskForm):
    drugName = StringField('Drug Name', validators=[DataRequired(), Length(1, 64)])
    drugRoute = SelectField('Route of Administration', choices=[('Uyo', 'Uyo'), ('Delta', 'Asaba')])
    drugDose = IntegerField('Drug Dosage', validators=[DataRequired()])
    drugStrenght = IntegerField('Dosage Available', validators=[DataRequired()])
    drugDuration = StringField('Duration of Use', validators=[DataRequired()])
    submit = SubmitField('Dispensed')


class AddressesForm(FlaskForm):
    """A form for one or more addresses"""
    drug = FieldList(FormField(Drug), min_entries=2)