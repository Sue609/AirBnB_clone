#!/usr/bin/python3
"""
    The base model of AirBnB project
"""
from datetime import datetime
import uuid


class BaseModel:
    """
        Base class
    """
    def __init__(self):
        """ Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints class attributes"""
        print('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.to_dict()))  
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.to_dict()))


    def save(self):
        """ save """
        self.updated_at = datetime.now()


    def to_dict(self):
        """ Returns dict representation of class instance """
        result = self.__dict__.copy()
        result['__class__'] =  self.__class__.__name__
        result['id'] = self.id
        result['updated_at'] = self.updated_at.isoformat()
        result['created_at'] = self.created_at.isoformat()
        return (result)
