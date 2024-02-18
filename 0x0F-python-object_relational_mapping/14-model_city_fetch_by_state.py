#!/usr/bin/python3
""" SQLAlchemy Practicing"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker()(bind=engine)
    cities = session.query(City).all()

    state = session.query(State).filter_by(id=cities[0].state_id).first()
    for city in cities:
        if state.id != city.state_id:
            state = session.query(State).filter_by(id=city.state_id).first()
        print(f'{state.name}: ({city.id}) {city.name}')
