#!/usr/bin/python3
"""module using sqlalchemy for queries"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, contains_eager
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://:{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Query = session.query(City).join(City.state)\
                   .options(contains_eager(City.state))\
                   .order_by(City.id,)\
                   .all()
    for city in Query:
        print(f"{city.id}: {city.name} -> {city.state.name}")
