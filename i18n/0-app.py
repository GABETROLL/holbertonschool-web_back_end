#!/usr/bin/env python3
import flask

app = flask.Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    """
    Returns the 0th template.
    Has "Welcome to Holberton" as page <title>
    and "Hello world" as the <h1>.
    """
    return flask.render_template("0-index.html")
