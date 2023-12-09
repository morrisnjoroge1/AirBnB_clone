#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to JSON file and deserializes JSON file to instances
    Args:
        __file_path(string): has the extension file.json
        __objects(dict): empty
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key, obj in FileStorage.__objects.items():
            json_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as myfile:
            json.dumps(json_obj, myfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as myfile:
                json_obj = json.load(myfile)
            for a in json_obj.values():
                cls_name = a["__class__"]
                del a["__class__"]
                self.new(eval(cls_name)(**a))
        except FileNotFoundError:
            return
