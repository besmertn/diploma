from flask import Blueprint

bp = Blueprint('sensor', __name__)

from diploma.sensor import routes
