#!/usr/bin/python3
"""
a script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    inherits from Base (imported from model_state)
    links to the MySQL table cities
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string of 128
    characters and can’t be null
    class attribute state_id that represents a column of an integer,
    can’t be null and is a foreign key to states.id

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
