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
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    name_search = sys.argv[4]

    engine = create_engine("mysql+mysqldb//{}:{}@localhost:3306/{}".
                           format(db_user, db_passwd, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    match = None
    for state in session.query(State).filter(State.name == name_search).all():
        match = state.id
    if match:
        print(match)
    else:
        print('Not found')
    session.close()
