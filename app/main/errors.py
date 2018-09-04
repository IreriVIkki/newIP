from flask import render_template

# Importing the main application since it is the only application that will use this erreo handling class
from . import main


# defining a function that will route the user to an error html file when user searches for an item that does not exist
@main.errorhandler(404)
def four_Ow_four(error):
    return render_template('fourOwfour.html'), 404
