#!/usr/bin/python3
"""
This module intorduces a new class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class inherits from the BaseModel.
    It shows the city where the AIRBNB user wants to stay.
    """

    state_id = ""
    name = ""
