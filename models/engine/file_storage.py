#!/usr/bin/python3
"""
    FileStorage module
"""
import json
import models


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
        """Serializes __objects to a JSON file (__file_path)."""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            serialized_obj = json.dumps(obj_dict)
            file.write(serialized_obj)

    def reload(self):
        """ deserialize the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                deserialized_obj = json.load(file)
                self.__objects = deserialized_obj
        except (FileNotFoundError, json.JSONDecodeError):
            self.__objects = {}

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
