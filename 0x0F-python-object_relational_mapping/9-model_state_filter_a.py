#!/usr/bin/python3
"""
script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session_1 = Session()

    states_1 = session_1.query(State).filter(State.name.contains('a'))
    if states_1 is not None:
        for state in states_1:
            print('{0}: {1}'.format(state.id, state.name))
