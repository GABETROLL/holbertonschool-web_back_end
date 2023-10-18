#!/usr/bin/env python3
"""
Exercise 0: Setup a basic app
"""
import flask
from os import environ

app = flask.Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    Returns the 0th template.
    Has "Welcome to Holberton" as page <title>
    and "Hello world" as the <h1>.
    """
    return flask.render_template("0-index.html")


if __name__ == "__main__":
    app.run(
        environ.get("HOST"), environ.get("PORT")
    )
