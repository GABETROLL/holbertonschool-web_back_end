#!/usr/bin/env python3
""" Main 4
"""
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User

# Add new user to the DB (file)
user_email = "bobsession@hbtn.io"
user_clear_pwd = "fake pwd"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

# Create a new session for user
sa = SessionAuth()
session_id = sa.create_session(user.id)
print("User with ID: {} has a Session ID: {}".format(user.id, session_id))

# Create a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """
    Root path: Returns a string of the user corresponding
    to the test request's session cookie.

    If the cookie doesn't belong to a session
    (in 'sa'), or if there's no cookie,
    this function just returns "No user found\n".
    """
    request_user = sa.current_user(request)
    if request_user is None:
        return "No user found\n"
    return "User found: {}\n".format(request_user.id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
