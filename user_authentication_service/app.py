#!/usr/bin/env python3
"""
Flask app for signing 'User's in.
"""
import flask
from typing import Tuple
from auth import Auth

auth = Auth()
app = flask.Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def bienvenue() -> Tuple[flask.Response, int]:
    return flask.jsonify({"message": "Bienvenue"}), 200


@app.route("/users/", methods=["POST"], strict_slashes=False)
def users() -> Tuple[flask.Response, int]:
    """
    Endpoint for registering a new user.

    EXPECTS:

    Only POST method, with the following data:
    "email=<email> password=<password>".

    WITH 'curl':

    curl localhost:5000/users -d email '<email>' -d password '<password>'

    If a user with that email already exists,
    this endpoint should respond with the JSON:
        {"message": "email already registered"}
    and a response code of 400.

    Otherwise, this endpoint should respond with the JSON:
        {"email": "<registered email>", "message": "user created"}
    and a response code of 200.
    """
    EMAIL: str = flask.request.form.get("email")
    PASSWORD: str = flask.request.form.get("password")

    try:
        auth.register_user(EMAIL, PASSWORD)
    except ValueError:
        return flask.jsonify({"message": "email already registered"}), 400
    else:
        return flask.jsonify({"email": EMAIL, "message": "user created"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
