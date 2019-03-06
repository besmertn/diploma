from flask import Blueprint

bp = Blueprint('settings', __name__)

from diploma.settings import routes
