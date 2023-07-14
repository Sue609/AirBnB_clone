#!/usr/bin/python3
"""
This module introduces a new class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This classinherits from the BaseModel.
    It has public class attributes.
    """

    place_id = ""
    user_id = ""
    text = ""
