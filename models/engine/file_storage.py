#!/usr/bin/python3
"""This module defines a class "FileStorage" that serializes and
deserializes instances to and from a JSON file."""

import json  # We need json to convert dictionary to JSON string and vice versa
from models.base_model import BaseModel  # We need to use the BaseModel class


class FileStorage:
    """A class to manage the storage of all our instances."""

    __file_path = "file.json"  # Where we'll store and load our data
    __objects = {}  # Here we will store all objects

    def all(self):
        """Returns all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to our storage."""
        # The key is the class name and id combined
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # The value is the object itself
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes our objects and saves them to a file."""
        # We'll populate this dictionary then write it to a file
        dict_objects = {}
        for key, value in FileStorage.__objects.items():
            # Convert objects to a dictionary before saving
            dict_objects[key] = value.to_dict()
        # Open the file
        with open(FileStorage.__file_path, 'w') as f:
            # Convert dict_objects to a JSON string and write it to a file
            json.dump(dict_objects, f)

    def reload(self):
        """Loads objects from the file and deserializes them."""
        try:
            # Open the file
            with open(FileStorage.__file_path, 'r') as f:
                # Load a JSON string from the file and convert it
                # to a dictionary
                dict_objects = json.load(f)
            for key, value in dict_objects.items():
                # Convert the dictionary to objects and store them
                FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            # If the file does not exist, do nothing.
            pass
