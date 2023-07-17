#!/usr/bin/python3
"""
    FileStorage module
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Class filestorage: serializes instances to JSON
    and deserializes JSON files to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns __objects(instance) dictionary """
        return (self.__objects)

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = '{}.{}'.format(obj.__class__.__name__, id(obj))
        value = obj
        FileStorage.__objects[key] = value

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict = {obj: self.__objects[obj].to_dict() for
                   obj in self.__objects.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            objdict = {}
            with open(self.__file_path, "w") as f:
                json.dump(objdict, f)

    def _deserialize_objects(self):
        """
        Method that correctly manages the serialization and
        deserialization of other classes.
        """

        classes = {
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review,
        }
        with open(self.__file_path, "r") as file:
            data = json.load(file)
            for obj_id, obj_attrs in data.items():
                clas_name = obj_attrs['__class__']
                if class_name in classes:
                    self.__objects[obj_id] = classes[class_name](**obj_attrs)
                else:
                    self.__objects[obj_id] = BaseModel(**obj_attrs)
