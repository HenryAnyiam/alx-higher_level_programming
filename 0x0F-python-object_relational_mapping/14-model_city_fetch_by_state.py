#!/usr/bin/python3
"""module using sqlalchemy for queries"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://:{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Query = session.query(City.id.label('id'), City.name.label
                          ('name'), State.name.label('state')).join(
                           State).filter(City.state_id ==
                                         State.id).order_by(City.id)
    for i in Query:
        print(f"{i.state}: ({i.id}) {i.name}")
