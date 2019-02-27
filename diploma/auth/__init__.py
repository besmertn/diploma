from flask import Blueprint

bp = Blueprint('auth', __name__)

from diploma.auth import auth, emails, forms, routes
