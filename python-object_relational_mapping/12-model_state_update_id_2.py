#!/usr/bin/python3
""" Update a state """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argb[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(user, passwd, db), pool_pre_ping=True)


    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).get(2)  # get the State with id = 2

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()