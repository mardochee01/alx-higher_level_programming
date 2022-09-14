#!/usr/bin/python3

"""
Python file similar to model_state.py
named model_city.py that contains
the class definition of a City
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    inherits from Base
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
