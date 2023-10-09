#!/usr/bin/env python3
"""
Defines the 'User' SQLAlchemy model for an SQL table named 'users'.
"""
from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(DeclarativeBase):
    """
    Base SQLAlchemy model
    """
    pass


class User(Base):
    """
    User ORM for 'users' table.

    Contains an 'id' foreign key,
    non-nullable 'email' and 'hashed_password' keys,
    and nullable 'session_id' and 'reset_token' keys.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    session_id: Mapped[str]
    reset_token: Mapped[str]

