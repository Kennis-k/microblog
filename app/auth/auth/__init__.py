from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth.auth import routes