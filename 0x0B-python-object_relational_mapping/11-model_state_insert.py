#!/usr/bin/python3
"""10-model_state_my_get.py"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import insert

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.
                           argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(State(name="Louisiana"))
    results = session.query(State.id, State.name).filter(
                            State.name == "Louisiana").first()
    print("{}".format(results.id))
    session.commit()