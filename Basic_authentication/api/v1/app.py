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

from api.v1.auth.auth import Auth, BasicAuth


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
# Fulfill sdabove docstring
if os.environ["AUTH_TYPE"] == "basic_auth":
    auth = BasicAuth()
else:
    auth = Auth()


@app.before_request
def authenticate() -> None:
    """
    Before doing anything with a request,

    This function
    checks if the URL path the user is requesting
    requires authorization.
    """
    if auth is None:
        return

    if not auth.require_auth(
        request.path,
        ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    ):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


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
