#!/usr/bin/env python3
"""
Exercise 1: Create a 'flask_babel.Babel' object named 'babel',
create a 'Config' class with the available languages,
add "en" as 'babel's default language and "UTC" as
'babel's default timezone,
and call 'app.config.from_object(Config)'.
"""
import flask
import flask_babel
from typing import Union
from os import environ


class Config:
    """
    Contains the allowed languages
    and default timezone for 'babel'.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = flask.Flask(__name__)
app.config.from_object(Config)
babel = flask_babel.Babel(app)


@app.route("/", strict_slashes=False)
def home() -> flask.Response:
    """
    Returns the 0th template.
    Has "Welcome to Holberton" as page <title>
    and "Hello world" as the <h1>.
    """
    return flask.render_template("1-index.html")


if __name__ == "__main__":
    app.run(
        environ.get("HOST"), environ.get("PORT")
    )
