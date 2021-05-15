""" Build a simple calculator with Flask, which uses URL query 
    parameters to get the numbers to calculate with.

    Make a Flask app that responds to 4 different routes. 
    Each route does a math operation with two numbers, a and b, 
    which will be passed in as URL GET-style query parameters.
"""

import operations

from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def add_page():
    """Gets a & b, adds the two, returns answer"""
    a = request.args.get("a")
    b = request.args.get("b")
    return str(operations.add(int(a), int(b)))


@app.route('/sub')
def subtract_page():
    """Gets a & b, subtracts the two, returns answer"""
    a = request.args.get("a")
    b = request.args.get("b")
    return str(operations.sub(int(a), int(b)))


@app.route('/mult')
def multiply_page():
    """Gets a & b, multiplies the two, returns answer"""
    a = request.args.get("a")
    b = request.args.get("b")
    return str(operations.mult(int(a), int(b)))


@app.route('/div')
def divide_page():
    """Gets a & b, divides the two, returns answer"""
    a = request.args.get("a")
    b = request.args.get("b")
    return str(operations.div(int(a), int(b)))
