from flask import Blueprint

main = Blueprint('main', __name__)

# i import views at this point to avoid circular dependancies
from . import views, errors
