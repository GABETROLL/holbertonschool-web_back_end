#!/usr/bin/env python3
"""
Contains class 'SessionAuth'.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Built to keep track of the user's session
    tokens in 'user_id_by_session_id',

    and making a new session and associating it
    with the user when a user logs in cold.

    'user_id_by_session_id' is a dictionary
    of SESSION UUIDs and USER IDs.
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

        Generates a new session UUID,
        assigns it to 'user_id' in this class' dictionary,

        and returns the SESSION UUID.
        """
        if user_id is None or type(user_id) != str:
            return None

        SESSION_ID: uuid.UUID = uuid.uuid4()

        self.user_id_by_session_id[SESSION_ID]: uuid.UUID = user_id

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

        return self.user_id_by_session_id.get(session_id, default=None)
