#!/usr/bin/env python3
"""
Exercise 2: Use the 'babel.localeselector'
to find the best matching available language
to give to the user.
"""
import flask
import flask_babel
from typing import Union
from os import environ


app = flask.Flask(__name__)
babel = flask_babel.Babel(app)


class Config:
    """
    Contains the allowed languages
    and default timezone for 'babel'.
    """
    LANGUAGES = ["en", "fr"]


babel.default_locale = Config.LANGUAGES[0]
babel.default_timezone = "UTC"

app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Returns the language from 'app.config["LANGUAGES"]'
    that best matches the languages in the request's
    'Accept-Language' header,
    using:

    return flask.request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )
    """
    return flask.request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


@babel.timezoneselector
def get_timezone() -> str:
    """
    Returns the default timezone, UTC.
    """
    return "UTC"


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
