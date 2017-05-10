from . import main
from flask import render_template
from .forms import AddressesForm


@main.route('/')
@main.route('/index')
def index():
    drug = [{"drugName": "Amoxicillin"}]
    user_addresses = [{"name": "First Address"},
                      {"name": "Second Address"}]
    form = AddressesForm()
    return render_template("firstform.html", form=form)
