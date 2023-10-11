"""
Flask app for signing 'User's in.
"""
import flask
from typing import Tuple

app = flask.Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def bienvenue() -> Tuple[flask.Response, int]:
    return flask.jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
