#!/usr/bin/python3
"""module using sqlalchemy for queries"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://:{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(func.binary(State.name)
                                           .like("%a%")).first()
    while instance:
        session.delete(instance)
        instance = session.query(State).filter(func.binary(State.name)
                                               .like("%a%")).first()
    session.commit()
