#!/usr/bin/env python3
"""
Contains class 'SessionAuth'.
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from typing import Union


class SessionAuth(Auth):
    """
    Built to keep track of the user's session
    tokens in 'user_id_by_session_id',

    and making a new session and associating it
    with the user when a user logs in cold.

    'user_id_by_session_id' is a dictionary
    of SESSION UUID strings and USER IDs.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        If 'user_id' is None        -> None
        If 'user_id' is not a 'str'
        (EVEN IF IT'S AN INSTANCE
        OF A CHILD CLASS OF 'str')  -> None

        ASSUMES THAT 'user_id' IS A SAFE & VALID USER ID,
        FIRST CREATED WITH USER CREDENTIALS.

        Generates a new session UUID string,
        assigns it to 'user_id' in this class' dictionary,

        and returns the SESSION UUID.
        """
        if user_id is None or type(user_id) != str:
            return None

        SESSION_ID: str = str(uuid.uuid4())

        self.user_id_by_session_id[SESSION_ID] = user_id

        return SESSION_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the ID of the user that owns
        the 'session_id'.

        ASSUMING THAT THE 'session_id' COULD HAVE ONLY BEEN
        KNOWN BY THE USER THAT OWNS THE 'session_id'.
        """
        if session_id is None or type(session_id) != str:
            return None

        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None) -> Union[User, None]:
        """
        ASSUMING THAT 'request' IS A VALID
        AND SAFE 'flask.request' from the user,

        and that 'request' contains the user's
        VALID SESSION COOKIE,

        This method returns the user's
        'models.user.User' representation,
        as a way to allow the user in.

        If 'request' is None, the cookie is missing,
        or the cookie is invalid (for example,
        the session expired or never existed),
        this method returns None instead.
        """

        if request is None:
            return None

        SESSION_COOKIE = self.session_cookie(request)

        # print(SESSION_COOKIE)

        USER_ID = self.user_id_for_session_id(SESSION_COOKIE)

        # print(f"{self.user_id_by_session_id = }")
        # print(RESULT)

        USER: User = User.get(USER_ID)
        return USER

    def destroy_session(self, request=None) -> bool:
        """
        If 'request' is None, this method returns False.

        If the user 'request' doesn't have the
        session ID cookie, this method returns False.

        ASSUMING THAT 'request' IS 'flask.request',
        AND THAT 'request' IS SAFE AND VALID,

        this method uses the request's cookies sent by the user,
        which should contain the session ID cookie,
        then deletes the session, logging off the user.

        Returns weather or not a session was killed.
        """
        if request is None:
            return False

        SESSION_ID: str = self.session_cookie(request)

        if SESSION_ID is None:
            return False

        if self.user_id_for_session_id(SESSION_ID) is None:
            return False

        del self.user_id_by_session_id[SESSION_ID]
        return True
