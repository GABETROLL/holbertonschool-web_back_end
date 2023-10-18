#!/usr/bin/env python3
"""
Exercise 0: Setup a basic app
"""
import flask
import flask_babel

app = flask.Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    DEFAULT_TIMEZONE = "UTC"


babel = flask_babel.Babel(
    app,
    BABEL_DEFAULT_LOCALE=Config.LANGUAGES[0],
    BABEL_DEFAULT_TIMEZONE=Config.DEFAULT_TIMEZONE
)


@app.route("/", strict_slashes=False)
def home():
    """
    Returns the 0th template.
    Has "Welcome to Holberton" as page <title>
    and "Hello world" as the <h1>.
    """
    return flask.render_template("0-index.html")
