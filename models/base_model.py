#!/usr/bin/python3
"""
The base_model module of the AirBnB webapp
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
        Args:
            *args: Variable length of arguement list.
            **kwargs: Arbitrary keyword arguements.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """
        Prints and returns attributes of a given class
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
         Updates the public instance attribute 'updated_at'
         with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns dict representation of a class instance
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['updated_at'] = self.updated_at.isoformat()
        result['created_at'] = self.created_at.isoformat()
        return (result)


if __name__ == '__main__':
    unittest.main()
