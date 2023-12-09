#!/usr/bin/python3
"""creatimg a class user that inherits from basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user body

    Args:
        email(str): user email and is an empty string
        password(str): an empty string of the user password
        first_name(str): empty string for the user's frist name
        last_name(str): empty string fot the user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
