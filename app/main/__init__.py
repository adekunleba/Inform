from flask import Blueprint

"""
This is the initialization for the main Bluepring
"""
main = Blueprint('main', __name__)

from . import views
