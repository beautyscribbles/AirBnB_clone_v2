#!/usr/bin/python3
"""script_that_starts a Flask web_application"""
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """Return_two_words"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def route_hbnb():
    """Return_a_word"""
    return "HBNB"


@app.route('/c/<path:subpath>', strict_slashes=False)
def route_c(subpath):
    """Return_subpath"""
    return "C {}".format(escape(subpath).replace('_', ' '))


@app.route('/python', defaults={'subpath': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:subpath>', strict_slashes=False)
def route_python(subpath):
    """Return_subpath"""
    return "Python {}".format(escape(subpath).replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def route_number(num):
    """Return_only_if_num is_a_int"""
    return "{} is a number".format(escape(num))


@app.route('/number_template/<int:num>', strict_slashes=False)
def route_template(num):
    """Return a file HTML only_if_num is_a_int"""
    return render_template("5-number.html", n=num)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
