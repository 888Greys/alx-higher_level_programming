#!/usr/bin/python3
"""
Python file similar to model_state.py named
model_city.py that contains the class definition of a City.
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Python file similar to model_state.py named
    model_city.py that contains the class definition of a City.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    session_1 = Session()

    results_1 = session_1.query(City, State).join(State)

    for city, state in results_1.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session_1.commit()
    session_1.close()
