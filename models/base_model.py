#!/usr/bin/python3
"""create BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines all the common attributes"""
    
    def __init__(self, *args, **kwargs):
        """
        initiliazes the basemodel class

        Args:
            *args(): unused
            *kwargs(dict): key and value pairs
        """
        timeformat = 'Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datatime.strptime(value, timeformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the public attribute at the updated_at with current date
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys and values of __dict__
        """
        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = self.__class__.__name__
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        return dict_cpy

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
