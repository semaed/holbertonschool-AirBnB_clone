#!/usr/bin/python3
"""This module defines a class "FileStorage" that serializes and
deserializes instances to and from a JSON file."""

import json  # We need json to convert dictionary to JSON string and vice versa
import os    # import os module used for file path operations
from models.user import User  # Import the User class
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A class to manage the storage of all our instances."""

    __file_path = "file.json"  # Where we'll store and load our data
    __objects = {}  # Here we will store all objects

    def all(self):
        """Returns all objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to our storage."""
        # Create the key as <class name>.<id>
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # Add object to dictionary
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes our objects and saves them to a file."""
        # Convert objects to dict representation
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        # Open file in write mode
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            # Write dictionary to file as JSON
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects
        """
        # Check if file exists
        if os.path.exists(self.__file_path):
            # Open file in read mode
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                # Load JSON file to dictionary
                obj_dict = json.load(f)
            # Import BaseModel here to avoid circular import
            from models.base_model import BaseModel
            # Convert dict to objects and add them to __objects
            for k, v in obj_dict.items():
                if v['__class__'] == 'BaseModel':
                    self.__objects[k] = BaseModel(**v)
                elif v['__class__'] == 'User':
                    self.__objects[k] = User(**v)
                elif v['__class__'] == 'State':
                    self.__objects[k] = State(**v)
                elif v['__class__'] == 'City':
                    self.__objects[k] = City(**v)
                elif v['__class__'] == 'Amenity':
                    self.__objects[k] = Amenity(**v)
                elif v['__class__'] == 'Place':
                    self.__objects[k] = Place(**v)
                elif v['__class__'] == 'Review':
                    self.__objects[k] = Review(**v)
