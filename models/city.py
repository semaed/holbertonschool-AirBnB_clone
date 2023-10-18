#!/usr/bin/python3
"""Module containing the City
"""

from models.base_model import BaseModel

# Define a class called City that inherits from BaseModel
class City(BaseModel):
    """ City class that inherits from BaseModel """
    state_id = ""  # It will be the State.id
    name = ""  # Define attributes 'state_id' and 'name'
