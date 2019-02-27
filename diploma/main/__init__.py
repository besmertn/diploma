from flask import Blueprint

bp = Blueprint('main', __name__)

from diploma.main import accuweather, routes
