#!/usr/bin/env python3
"""
Exercise 4: Implement the
"login_as=<username>" URL parameter.

Make a pretend user preference database
of locales and timezones in this module,
called 'users'.

Add a login status message to the template
(templates/5-index.html) in all of the available
languages.
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
babel = flask_babel.Babel(
    app,
    Config.BABEL_DEFAULT_LOCALE,
    Config.BABEL_DEFAULT_TIMEZONE
)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


@babel.timezoneselector
def get_timezone() -> str:
    """
    Returns the default timezone, UTC.
    """
    return "UTC"


def get_user() -> Union[dict, None]:
    """
    Returns the corresponding user in <users>
    for the "login_as=<USER_ID>" URL parameter.

    If the parameter wasn't defined, or the <USER_ID>
    is invalid, this function returns None.
    """
    USER_ID_STR: Union[str, None] = flask.request.args.get(
        "login_as"
    )
    # print(f"USER_ID={USER_ID_STR}")

    try:
        USER_ID: int = int(USER_ID_STR)
    except Exception:
        return None
    else:
        RESULT = users.get(USER_ID)
        # print(f"RESULT={RESULT}")
        return RESULT


@app.before_request
def before_request():
    """
    Gets the user from <get_user()>,
    and stores it in <flask.g.user>,
    for the 'templates/5-index.html' template to use.
    """
    USER: Union[dict, None] = get_user()
    flask.g.user = USER


@app.route("/", strict_slashes=False)
def home() -> flask.Response:
    """
    Returns the 0th template.
    Has "Welcome to Holberton" as page <title>
    and "Hello world" as the <h1>.
    """
    return flask.render_template("5-index.html")


if __name__ == "__main__":
    app.run(
        environ.get("HOST"), environ.get("PORT")
    )
