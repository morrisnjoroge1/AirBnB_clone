#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """class city that inherits from basemodel class
    Args:
        state_id(str): user's state id, empty string
        name(str): user's name, empty string
    """
    state_id = ""
    name = ""
