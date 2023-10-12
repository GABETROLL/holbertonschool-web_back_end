#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
from typing import Union


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Creates a new User object using 'email' and 'hashed_password'
        correspondingly, adds the data to 'self's DB file,
        and returns it.
        """
        RESULT: User = User(
            email=email,
            hashed_password=hashed_password,
        )

        self._session.add(RESULT)
        self._session.commit()

        return RESULT

    def find_user_by(self, **kwargs) -> User:
        """
        Finds the first row in the 'users' table
        that matches the 'kwargs'.

        Then, returns the row as a User object.

        If the 'kwargs' don't match the definition of 'User',
        this method raises 'InvalidRequestError'.

        If no matching 'User' row is found,
        this method raises 'NoResultFound'.
        """
        RESULT: Union[User, None] = self._session.query(User) \
            .filter_by(**kwargs) \
            .first()

        if RESULT is None:
            raise NoResultFound

        return RESULT

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Finds the 'User' with 'user_id' as its 'id'
        in 'self's DB file, and updates the row with
        'kwargs'.

        This method uses 'self.find_user_by(id=user_id)'
        to find the user.

        So, if a user with 'user_id' as
        its 'id' doesn't exist, this method also raises
        NoResultFound.

        And if the 'kwargs' don't have the correct attributes,
        this method raises a ValueError.
        """
        USER: User = self.find_user_by(id=user_id)

        if 'id' in kwargs:
            raise ValueError("Cannot update 'id' of 'User'.")

        for attr, value in kwargs.items():
            if attr not in USER.__dict__.keys():
                raise ValueError(f"'User' object has no attribute '{attr}'")
            setattr(USER, attr, value)
