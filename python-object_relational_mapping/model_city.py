#!/usr/bin/python3
"""
This module defines the City class that maps to the cities table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that represents a city in the 'cities' table.
    Attributes:
        id (int): Auto-incremented primary key
        name (str): Name of the city
        state_id (int): Foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
