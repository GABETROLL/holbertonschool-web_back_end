#!/usr/bin/env python3
"""
Contains the 'app_views' flask blueprint,
and all of the paths of this site,
which should all start with '/api/v1/'.
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()
