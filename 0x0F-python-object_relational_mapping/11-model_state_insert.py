#!/usr/bin/python3

"""
script that prints the State object
with the name passed as argument from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    new_obj = State(name="Louisiana")
    session.add(new_obj)
    session.commit()

    print(new_obj.id)

    session.close()
