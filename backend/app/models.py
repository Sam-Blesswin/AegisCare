# This file defines the database models for the application using SQLAlchemy ORM.
# It includes two models: User and Transaction.

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# The models are defined using SQLAlchemy's declarative base, which allows for
# easy mapping of Python classes to database tables.
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    asset = Column(String)
    action = Column(String)
    amount = Column(Float)
