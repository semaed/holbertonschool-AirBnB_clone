#!/usr/bin/python3
"""This is the console module.

This module starts the command interpreter using cmd module.
"""
# Import the cmd module which provides a framework
# for a command-line interpreter
import cmd
from models.base_model import BaseModel  # Import the BaseModel class
from models.user import User  # Import the User class
from models.state import State  # Import the State class
from models.city import City  # Import the City class
from models.amenity import Amenity  # Import the Amenity class
from models.place import Place  # Import the Place class
from models.review import Review  # Import the Review class
from models import storage  # Import the storage object
import shlex


class HBNBCommand(cmd.Cmd):
    """This class is the command interpreter.

    It inherits from cmd.Cmd which means it can make use of the cmd module.
    """

    # The prompt attribute of cmd.Cmd sets the prompt
    prompt = '(hbnb) '

    # Create a dictionary to map class names to classes
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    # Below are the methods that implement the functionality of the commands.

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True  # A True return value causes the cmdloop() to exit.

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = arg.split()  # Split the arguments
        if len(args) < 1:  # Check if class name is missing
            print("** class name missing **")
        elif args[0] not in self.classes:  # Check if class doesn't exist
            print("** class doesn't exist **")
        else:
            # Create new instance # Create new instance
            new_instance = self.classes[args[0]]()
            new_instance.save()  # Save it
            print(new_instance.id)  # Print the id

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()  # Split the arguments
        if len(args) == 0:  # Check if class name is missing
            print("** class name missing **")
        elif args[0] not in self.classes:  # Check if class doesn't exist
            print("** class doesn't exist **")
        elif len(args) == 1:  # Check if id is missing
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]  # Create key as <class name>.<id>
            if key not in storage.all():  # Check if instance doesn't exist
                print("** no instance found **")
            else:
                print(storage.all()[key])  # Print the instance

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()  # Split the arguments
        if len(args) == 0:  # Check if class name is missing
            print("** class name missing **")
        elif args[0] not in self.classes:  # Check if class doesn't exist
            print("** class doesn't exist **")
        elif len(args) == 1:  # Check if id is missing
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]  # Create key as <class name>.<id>
            if key not in storage.all():  # Check if instance doesn't exist
                print("** no instance found **")
            else:
                storage.all().pop(key)  # Delete the instance
                storage.save()  # Save changes to the JSON file

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()  # Split the arguments
        # Check if class doesn't exist
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            # Print all instances based or not on the class name
            print([str(v) for k, v in storage.all().items() if args[0] in k])

    def do_update(self, arg):
        """Updates an instance based on the class name and if by
        adding or updating attribute (save the change into the JSON file)\n"""
        if not arg:
            print("** class name missing **")
            return

        li_arg = shlex.split(arg)
        if len(li_arg) < 2:
            print("** instance id missing **")
            return

        try:
            model = storage.all()[f"{li_arg[0]}.{li_arg[1]}"]
            if len(li_arg) < 3:
                print("** attribute name missing **")
            elif len(li_arg) < 4:
                print("** value missing **")
            else:
                attr_name = li_arg[2]
                attr_value = li_arg[3]
                if attr_value.startswith('"') and attr_value.endswith('"'):
                    attr_value = attr_value[1:-1]
                setattr(model, attr_name, attr_value)
                model.save()
        except KeyError:
            print("** no instance found **")

    def emptyline(self):
        """Do nothing when hit enters\n"""
        pass


if __name__ == '__main__':
    """Only run the following code when this file is not imported."""
    HBNBCommand().cmdloop()  # Start the cmd loop
