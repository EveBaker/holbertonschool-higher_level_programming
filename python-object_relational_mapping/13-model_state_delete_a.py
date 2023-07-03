#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "main":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for item in session.query(State).filter(State.name.like
                                        ('%a%')).order_by(State.id):
    session.delte(item)

    session.commit()
    session.close()