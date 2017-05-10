from . import db
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField


class AddressEntryForm(FlaskForm):
    name = StringField()


class AddressesForm(FlaskForm):
    """A form for one or more addresses"""
    addresses = FieldList(FormField(AddressEntryForm), min_entries=2)
