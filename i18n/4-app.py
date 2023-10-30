#!/usr/bin/env python3
"""
Exercise 4: In 'get_locale',
if the user requests "locale=<language>"
in the request URL,
and the language is available (check in <Config.LANGUAGES>
or in <app.config["LANGUAGES"]),
return that language instead ofwhat was being returned
there in exercise 3.
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


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Checks that the request URL contains "?locale=<language>",
    and returns the language code specified in the URL, if it is available.

    If the language in the URL is not present,
    or if the language isn't available in this app
    (available languages are defined in this module,
    in <Config.LANGUAGES>),
    this function:

    Returns the language from 'app.config["LANGUAGES"]'
    that best matches the languages in the request's
    'Accept-Language' header,
    using:

    return flask.request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )
    """
    LOCALE_ARG: Union[str, None] = flask.request.args.get("locale", None)

    if LOCALE_ARG is not None and LOCALE_ARG in app.config["LANGUAGES"]:
        return LOCALE_ARG

    return flask.request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


@app.route("/", strict_slashes=False)
def home() -> flask.Response:
    """
    Returns the 0th template.
    Has "Welcome to Holberton" as page <title>
    and "Hello world" as the <h1>.
    """
    return flask.render_template("4-index.html")


if __name__ == "__main__":
    app.run(
        environ.get("HOST"), environ.get("PORT")
    )
