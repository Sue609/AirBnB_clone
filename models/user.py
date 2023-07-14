#!/usr/bin/python3
"""
A class user that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A new class that will inherit from the basemodel class.
    Initialization of newpublic class attributes.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
