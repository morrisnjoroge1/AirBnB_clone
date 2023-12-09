#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """class review body
    Args:
        place_id(str): place id
        user_id(str): user id
        text(str): text
    """
    place_id = ""
    user_id = ""
    text = ""
