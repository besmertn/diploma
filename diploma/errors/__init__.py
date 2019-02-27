from flask import Blueprint

bp = Blueprint('errors', __name__)

from diploma.errors import handlers
