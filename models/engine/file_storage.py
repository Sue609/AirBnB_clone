#!/usr/bin/python3
"""
    FileStorage module
"""
import json
import models


class FileStorage:
    """
        Class filestorage: serializes instances to JSON and deserializes JSON files to instances
    """
    __file_path__ = 'file.json'
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
        """ serializes __objects to a JSON file (__file_path)"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dicy[key] = value.to_dict()
        with open(self.__file_path__, 'w') as file:
            serialized_obj = json.dumps(self.__objects)
            file.write(serialized_obj)


    def reload(self):
        """ deserialize the JSON file to __objects """
        try:
            with open(self.__file_path__, 'r') as file:
                deserialized_obj = json.load(file)
                self.__objects = deserialized_obj
        except FileNotFoundError:
            pass
