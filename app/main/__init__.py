from flask import Blueprint

"""
This is the initialization for the main Blueprint
"""
main = Blueprint('main', __name__)

from . import views
