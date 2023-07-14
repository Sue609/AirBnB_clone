#!/usr/bin/python3
"""
    The base_model module of the AirBnB webapp
    It defines the classes that makes up the web App's logic
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
        BaseModel the Main class from which all other classes will inherit
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if (key == '__class__'):
                    pass
                elif (key == 'id'):
                    self.id = value
                elif (key == 'created_at'):
                    self.created_at = datetime.fromisoformat(value)
                elif (key == 'updated_at'):
                    self.updated_at = datetime.fromisoformat(value)
                elif (key == 'name'):
                    self.name = value

    def __str__(self):
        """
        Prints and returns attributes of a given class
        """
        print('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.to_dict()))
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.to_dict()))


    def save(self):
        """
        Updates public instances of a class and saves it to file
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()


    def to_dict(self):
        """
        Returns dict representation of a class instance
        """
        result = self.__dict__.copy()
        result['__class__'] =  self.__class__.__name__
        result['id'] = self.id
        result['updated_at'] = self.updated_at.isoformat()
        result['created_at'] = self.created_at.isoformat()
        return (result)
