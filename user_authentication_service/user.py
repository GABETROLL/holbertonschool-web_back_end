#!/usr/bin/env python3
"""
Defines the 'User' SQLAlchemy model for an SQL table named 'users'.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    User ORM for 'users' table.

    Contains an 'id' foreign key,
    non-nullable 'email' and 'hashed_password' keys,
    and nullable 'session_id' and 'reset_token' keys.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
