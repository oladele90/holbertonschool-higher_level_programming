#!/usr/bin/python3
"""model_state.py"""


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
"""Creates a base class"""


class State(Base):
    """Creates class called States that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
