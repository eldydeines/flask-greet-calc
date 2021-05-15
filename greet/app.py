""" Made a simple Flask app that responds to these routes with simple text messages:

    /welcome
        Returns “welcome”
    /welcome/home
        Returns “welcome home”
    /welcome/back
        Return “welcome back”
"""

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    """Simple welcome page"""
    return "welcome"

@app.route('/welcome/home')
def welcome_home_page():
    """Simple welcome home page"""
    return "welcome home"

@app.route('/welcome/back')
def welcome_back_page():
    """Simple welcome back page"""
    return "welcome back"