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
        """
        return self._session.query(User).filter_by(**kwargs).first()
