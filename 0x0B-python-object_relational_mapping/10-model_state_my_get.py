#!/usr/bin/python3
"""10-model_state_my_get.py"""


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
    results = session.query(State.id, State.name).filter_by(
                            name=sys.argv[4]).first()
    if results and results is not None:
        print("{}".format(results.id))
    else:
        print("Not found")
