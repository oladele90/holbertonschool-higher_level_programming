#!/usr/bin/python3
"""8-model_state_fetch_first.py"""


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
    results = session.query(State.id, State.name).first()
    if results:
        print("{}: {}".format(results.id, results.name))
    else:
        print("Nothing")
