#!/usr/bin/python3
""" SQLAlchemy Practicing """
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """ The table cities """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
