from flask import Blueprint

back_bp = Blueprint("back_bp", __name__)

from app.backoffice import models, routes
