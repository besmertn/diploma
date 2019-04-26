from flask import Blueprint

bp = Blueprint('statistic', __name__)

from diploma.statistic import routes
