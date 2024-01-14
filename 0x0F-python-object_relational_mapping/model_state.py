#!/usr/bin/python3
"""
script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base_1 = declarative_base()


class State(Base_1):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states'

    id_1 = Column(Integer, primary_key=True)
    name_1 = Column(String(128), nullable=False)
