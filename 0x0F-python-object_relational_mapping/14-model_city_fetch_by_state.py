#!/usr/bin/python3

"""
Script that prints all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(db_user, db_password,
                                   db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = session.query(State, City).order_by(
        City.id).filter(City.state_id == State.id)

    for obj in objs:
        print("{}: ({}) {}".format(obj.State.name, obj.City.id, obj.City.name))

    session.close()
