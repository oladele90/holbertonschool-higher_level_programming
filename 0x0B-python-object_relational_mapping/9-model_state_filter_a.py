#!/usr/bin/python3
"""9-model_state_filter_a.py"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.
                           argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    results = session.query(State.id, State.name)
    for id, name in session.query(State.id, State.name):
        if "a" in name:
            print("{}: {}".format(id, name))
