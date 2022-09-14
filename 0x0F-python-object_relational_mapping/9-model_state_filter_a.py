#!/usr/bin/python3

"""
script that lists all State objects
that contain the letter a from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(db_user, db_passwd, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).filter(
        State.name.like("%a%"))
    for state in states:
        print("{}: {}".format(State.id, State.name))
    session.close()
