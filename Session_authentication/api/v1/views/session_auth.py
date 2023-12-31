#!/usr/bin/env python3
"""
Contains the flask route '/api/v1/auth_session/login/',
which allows the user to login for the first time,
and creates a new session for the user.
"""
from api.v1.views import app_views
import flask
from models.user import User
from typing import List, Tuple
from api.v1.auth.session_auth import SessionAuth
import os


@app_views.route('/auth_session/login', methods=["POST"], strict_slashes=False)
def login():
    """
    Allows the user to send a POST flask.request
    with their email and password,
    so that they can log in for the first time,
    using SESSION AUTH this time.

    If the POST request has no email or password,
    this function responds with an error code of 400.

    If the credentials provided don't belong to
    a 'models.user.User' object in the DB
    (this function searches for the matching user
    with 'models.user.User.search'),
    this function returns the JSON
    {"error": "no user found for this email"},
    with a response code of 404.

    If the email in the POST request DOES BELONG TO
    A USER, but the password doesn't, this function returns
    the JSON {"error": "wrong password"}, with a response
    code of 401.

    If the user's POST request's 'form' contains
    a valid EMAIL and PASSWORD, this function
    CREATES A SESSION FOR THE USER, and SENDS
    the SESSION TOKEN to the user as a COOKIE.
    """
    from api.v1.app import auth

    EMAIL = flask.request.form.get("email", default=None)
    PASSWORD = flask.request.form.get("password", default=None)

    if EMAIL is None:
        return flask.jsonify({"error": "email missing"}), 400

    if PASSWORD is None:
        return flask.jsonify({"error": "password missing"}), 400

    USERS_WITH_EMAIL: List[User] = User.search({"email": EMAIL})

    if not USERS_WITH_EMAIL:
        return flask.jsonify({"error": "no user found for this email"}), 404

    # There should only ever be one user
    # with X email.
    assert len(USERS_WITH_EMAIL) == 1

    USER: User = USERS_WITH_EMAIL[0]

    if not USER.is_valid_password(PASSWORD):
        return flask.jsonify({"error": "wrong password"}), 401

    # No other auth type should be allowed.
    assert type(auth) == SessionAuth

    # Create user's session
    USER_SESSION_ID = auth.create_session(USER.id)

    # Create cookie
    SESSION_COOKIE_NAME: str = os.environ.get("SESSION_NAME")

    response: flask.Response = flask.make_response(
        flask.jsonify(USER.to_json())
    )
    response.set_cookie(SESSION_COOKIE_NAME, USER_SESSION_ID)

    return response


@app_views.route('/auth_session/logout',
                 methods=["DELETE"],
                 strict_slashes=False)
def logout() -> Tuple[flask.Response, int]:
    """
    Upon recieving a DELETE request from the user,

    This function tries to delete the user's session
    using 'auth.destroy_session(request)'.

    If something goes wrong, and the 'destroy_session'
    call returns False, this function returns
    False with a response code of 404.

    If destroying the session is successful,
    this function returns True with a response code
    of 200."""
    from api.v1.app import auth

    assert type(auth) == SessionAuth

    SESSION_DESTROYED: bool = auth.destroy_session(flask.request)

    if SESSION_DESTROYED:
        return flask.jsonify(True), 200
    else:
        return flask.jsonify(False), 404
