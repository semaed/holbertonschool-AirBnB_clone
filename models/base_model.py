#!/usr/bin/python3
"""
This module contains the BaseModel class which will be the base class for
other classes.
"""

# We import the uuid module to generate unique IDs
import uuid
# We import the datetime module to manage dates and times
from datetime import datetime


class BaseModel:
    """
    A base class that defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        This method is called when a new instance of the class is created.
        If kwargs is not empty, assigns attributes based on kwargs.
        Otherwise, assigns unique id and the current date/time.
        """
        if kwargs:
            # kwargs provided? We're recreating an instance from a dictionary.
            for key, value in kwargs.items():
                # Loop through each key-value pair.
                if key == 'created_at' or key == 'updated_at':
                    # If key is 'created_at'/'updated_at', convert string
                    # to datetime.
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    # Skip '__class__' key, not needed for attribute.
                    setattr(self, key, value)
                    # Set attribute on instance with key-value pair.
        else:

            # Create a unique ID for each instance
            self.id = str(uuid.uuid4())
            # Get the current date and time.
            now = datetime.now()

            # Set the 'created_at' attribute to the current date and time.
            # This marks when this instance was created.
            self.created_at = now

            # Get the current date and time for created_at and updated_at
            # Set the 'updated_at' attribute to the current date and time.
            # At creation, 'created_at' and 'updated_at' are the same.
            # Later, 'updated_at' will change whenever the instance is updated.
            self.updated_at = now

    def __str__(self):
        """
        This method returns a string representation of the instance.
        """
        # Format and return the string using f-string
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates the 'updated_at' attribute with the current date
        and time.
        """
        # Update the 'updated_at' attribute with the current date and time
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method returns a dictionary containing all keys/values of the
        instance's __dict__.
        """

        # Make a copy of the __dict__ dictionary
        dict_copy = self.__dict__.copy()

        # Add the class name to the dictionary
        dict_copy["__class__"] = self.__class__.__name__

        # Convert 'created_at' and 'updated_at' to strings in ISO format
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()

        # Return the dictionary
        return dict_copy
