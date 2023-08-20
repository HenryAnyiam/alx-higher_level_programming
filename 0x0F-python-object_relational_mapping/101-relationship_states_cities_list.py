#!/usr/bin/python3
"""module using sqlalchemy for queries"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://:{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Query = session.query(State).order_by(State.id)
    for state in Query:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
