#!/usr/bin/python3
"""
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    session_1 = Session()

    new_state = State(name="Louisiana")
    session_1.add(new_state)
    session_1.commit()

    print('{0}'.format(new_state.id))
    session_1.close()
