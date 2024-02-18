#!/usr/bin/python3
""" SQLAlchemy Practicing"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker()(bind=engine)

    states = session.query(State).all()

    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'    {city.id}: {city.name}')

    session.close()
