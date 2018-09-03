# start by making all the required imports
from flask import render_template
# import the blueprint application from this very same folder
from . import main
# import articles and sources classes for creating their respective objects
from ..models import Articles, Sources

# defining the homepage route


@main.route('/')
def index():
    #
    pass
