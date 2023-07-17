#!/usr/bin/python3
"""
The base_model module of the AirBnB webapp
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel the Main class from which all other classes will inherit
    """

    dt_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class
        Args:
            *args: Variable length of arguement list.
            **kwargs: Arbitrary keyword arguements.
        """
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
        else:
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], self.dt_format
            )
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], self.dt_format
            )
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Prints and returns attributes of a given class
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Delete the current instance from __objects, if it exists."""
        key = '{}.{}'.format(self.__class__.__name__, self.id)
        models.storage.all()[key] = self
        models.storage.save()

    def to_dict(self):
        """
        Returns dict representation of a class instance
        """
        result = self.__dict__.copy()
        result['__class__'] = type(self).__name__
        result['updated_at'] = self.updated_at.isoformat()
        result['created_at'] = self.created_at.isoformat()
        return result
