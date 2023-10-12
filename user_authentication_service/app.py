#!/usr/bin/env python3
"""
Flask app for signing 'User's in.
"""
import flask
from typing import Tuple, Optional
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

AUTH = Auth()
app = flask.Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def bienvenue() -> Tuple[flask.Response, int]:
    """
    Expects GET with nothing,
    responds with {"message": "Bienvenue"} and a status code of 200.
    """
    return flask.jsonify({"message": "Bienvenue"}), 200


@app.route("/users/", methods=["POST"], strict_slashes=False)
def users() -> Tuple[flask.Response, int]:
    """
    Endpoint for registering a new user.

    EXPECTS:

    Only POST method, with the following data:
    email=<email> password=<password>

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
    EMAIL: Optional[str] = flask.request.form.get("email")
    PASSWORD: Optional[str] = flask.request.form.get("password")

    try:
        AUTH.register_user(EMAIL, PASSWORD)
    except ValueError:
        return flask.jsonify({"message": "email already registered"}), 400
    else:
        return flask.jsonify({"email": EMAIL, "message": "user created"}), 200


@app.route("/sessions/", methods=["POST"], strict_slashes=False)
def login() -> flask.Response:
    """
    Logs a user in, and creates a session for them.

    EXPECTS:

    Only POST method, with the following data:
    email=<email> password=<password>

    WITH 'curl':

    curl localhost:5000/users -d email '<email>' -d password '<password>'

    If the user credentials aren't valid, this function calls
    flask.abort(401).

    Otherwise, this function creates a session for the user
    with 'AUTH.create_session', and sends:

    cookie: session_id=<SESSION ID>
    response data: {"email": <user email>, "message": "logged in"}
    with a response code of 200.
    """
    EMAIL: Optional[str] = flask.request.form.get("email")
    PASSWORD: Optional[str] = flask.request.form.get("password")

    if not AUTH.valid_login(EMAIL, PASSWORD):
        flask.abort(401)

    SESSION_ID: Optional[str] = AUTH.create_session(EMAIL)

    if SESSION_ID is None:
        flask.abort(401)

    response: flask.Response = flask.make_response(
        flask.jsonify({"email": EMAIL, "message": "logged in"})
    )
    response.set_cookie("session_id", SESSION_ID)

    return response


@app.route("/sessions/", methods=["DELETE"], strict_slashes=False)
def logout():
    """
    EXPECTS:
        cookie: session_id=<session id>

    If the cookie is invalid, this route responds with a
    status code of 403.

    Kills the user's session by replacing the User's
    'session_id' value with None.
    Redirects to "GET /".

    (The route for "GET /" is the top function in this file)
    """
    REQUEST_SESSION_ID_COOKIE: Optional[str] = \
        flask.request.cookies.get(
            "session_id"
        )

    if REQUEST_SESSION_ID_COOKIE is None:
        flask.abort(403)

    USER: Optional[User] = \
        AUTH.get_user_from_session_id(
            REQUEST_SESSION_ID_COOKIE
        )

    if USER is None:
        flask.abort(403)

    try:
        AUTH.destroy_session(USER.id)
    except NoResultFound:
        abort(403)

    return flask.redirect(flask.url_for('bienvenue'))


@app.route("/profile/", methods=["GET"], strict_slashes=False)
def profile() -> flask.Response:
    """
    EXPECTS:
        cookie: session_id=<session id>

    RESPONDS:
        If the cookie exists and is valid, this route responds with:
            {"email": <user email>"}
            and a status code of 200
        by returning a 'flask.Reponse' with the above data.
        Otherwise:
            This function calls 'flask.abort(403)'.
    """
    REQUEST_SESSION_ID_COOKIE: Optional[str] = \
        flask.request.cookies.get(
            "session_id"
        )

    if REQUEST_SESSION_ID_COOKIE is None:
        flask.abort(403)

    USER: Optional[User] = \
        AUTH.get_user_from_session_id(
            REQUEST_SESSION_ID_COOKIE
        )

    if USER is None:
        flask.abort(403)

    return flask.jsonify({"email": USER.email})


@app.route("/reset_password/", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> flask.Response:
    """
    EXPECTS:
        form data: email=<user's email>

    RESPONDS:
        {"email": <email>, "reset_token": <reset token>}
        and a status code of 200,
            if the form data contains "email", and the value
            is valid.
        or  status code of 403
            if the "email" data is missing or invalid.
    """
    EMAIL: Optional[str] = flask.request.form.get("email")

    if EMAIL is None:
        flask.abort(403)

    try:
        RESULT: str = AUTH.get_reset_password_token(EMAIL)
    except ValueError:
        flask.abort(403)

    return flask.jsonify({"email": EMAIL, "reset_token": RESULT})


@app.route("/reset_password/", methods=["PUT"], strict_slashes=False)
def update_password() -> flask.Response:
    """
    EXPECTS:
        form data:
            email=<User's email>
            reset_token=<reset_token>
            new_password=<new password>

    Updates the password of the User specified with the form data.
    If that User doesn't exist or doesn't have that reset token,

    this function responds with a code of 403, by calling 'flask.abort(403)'.

    RESPONDS:
        If the credentials and reset token are valid:
            data:
                {"email": <email>, "message": "Password updated"}
            code:
                200
        Otherwise:
            code:
                403
    """
    EMAIL: Optional[str] = flask.request.form.get("email")
    RESET_TOKEN: Optional[str] = flask.request.form.get("reset_token")
    NEW_PASSWORD: Optional[str] = flask.request.form.get("new_password")

    try:
        AUTH.update_password(RESET_TOKEN, NEW_PASSWORD)
    except ValueError:
        flask.abort(403)

    return flask.jsonify({"email": EMAIL, "message": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
