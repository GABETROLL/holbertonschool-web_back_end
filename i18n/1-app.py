#!/usr/bin/env python3
"""
Exercise 0: Setup a basic app
"""
import flask
import flask_babel
from os import environ


app = flask.Flask(__name__)
babel = flask_babel.Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    return flask.request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


@babel.timezoneselector
def get_timezone():
    return "UTC"


@app.route("/", strict_slashes=False)
def home():
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
