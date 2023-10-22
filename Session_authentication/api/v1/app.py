#!/usr/bin/env python3
"""
Route module for the API.

Defines the protocol for every request,
and deploys the correct type of authentication
based on the environment variable 'AUTH_TYPE'.

Also defines 3 URL paths and their responses.
(read below)
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
from models.user import User

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth: Auth = None
"""
Should be an instance of a child class of 'Auth',
depending on which authentication type is being
run on this server,

defined in the environment variable 'AUTH_TYPE'.
"""
# Fulfill above docstring
AUTH_TYPE: str = os.environ.get("AUTH_TYPE", None)

auth: Auth = None

if AUTH_TYPE == "basic_auth":
    # key may not exist.
    # IF the key doesn't exist, we treat its value as None.
    # and go with Auth.
    auth = BasicAuth()
elif AUTH_TYPE == "session_auth":
    auth = SessionAuth()
else:
    auth = Auth()


@app.before_request
def authenticate() -> None:
    """
    Before doing anything with a request,

    This function
    checks if the URL path the user is requesting
    requires authorization.

    If it does, this function then tries to validate
    the user's auth details.

    If the user hasn't sent an AUTH header
    nor a session cookie,
    this function aborts with a response code of
    401 (Unauthorized).

    This function responds to the request depending
    on the AUTH method, defined in 'auth',
    which is defined by the 'AUTH_TYPE' environment
    variable in the computer running this script,
    which should be the server.

    If the AUTH method (defined in the
    "AUTH_TYPE" environment variable) is Basic,
    and the user's request is also using Basic,
    this function attempts to validate the user's
    credentials and allows them in if they are correct.

    If the AUTH method the user is using is Basic,
    and 'auth' is currently 'SessionAuth',
    this function aborts with a response code of
    403.

    If the user has provided a session ID cookie,
    <IMPLEMENT...>

    Also assigns 'request.current_user' to the current
    user.
    """
    if auth is None:
        return

    if not auth.require_auth(
        request.path,
        [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/',
            '/api/v1/auth_session/login/'
        ]
    ):
        return

    AUTH_HEADER: str = auth.authorization_header(request)
    SESSION_COOKIE = auth.session_cookie(request)

    if AUTH_HEADER is None and SESSION_COOKIE is None:
        # User has not provided credentials,
        # nor has provided a session cookie.
        abort(401)

    # assert type(AUTH_HEADER) == str

    USER: User = auth.current_user(AUTH_HEADER)
    # (if the 'auth' type is 'SessionAuth',
    # the 'current_user' method being ran is the one
    # from 'Auth', which should automatically return None,
    # and forbid the user from using Basic AUTH,
    # instead of Session AUTH)

    if USER is None:
        # User doesn't have valid credentials,
        # or the user isn't using correct authorization.
        abort(403)

    # assert type(USER) == User

    request.current_user = USER


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Unauthorized (401) error handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def unauthorized(error) -> str:
    """
    Forbidden (403) error handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
