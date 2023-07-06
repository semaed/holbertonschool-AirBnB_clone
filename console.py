#!/usr/bin/python3
"""This is the console module.

This module starts the command interpreter using cmd module.
"""
# Import the cmd module which provides a framework
# for a command-line interpreter
import cmd
from models.base_model import BaseModel  # Import the BaseModel class
from models import storage  # Import the storage object


class HBNBCommand(cmd.Cmd):
    """This class is the command interpreter.

    It inherits from cmd.Cmd which means it can make use of the cmd module.
    """

    # The prompt attribute of cmd.Cmd sets the prompt
    prompt = '(hbnb) '

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
        elif args[0] != "BaseModel":  # Check if class doesn't exist
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()  # Create new instance
            new_instance.save()  # Save it

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()  # Split the arguments
        if len(args) == 0:  # Check if class name is missing
            print("** class name missing **")
        elif args[0] != "BaseModel":  # Check if class doesn't exist
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
        elif args[0] != "BaseModel":  # Check if class doesn't exist
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
        if len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            # Print all instances based or not on the class name
            print([str(v) for k, v in storage.all().items() if "BaseModel"
                   in k])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()  # Split the arguments
        if len(args) == 0:  # Check if class name is missing
            print("** class name missing **")
        elif args[0] != "BaseModel":  # Check if class doesn't exist
            print("** class doesn't exist **")
        elif len(args) == 1:  # Check if id is missing
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]  # Create key as <class name>.<id>
            if key not in storage.all():  # Check if instance doesn't exist
                print("** no instance found **")
            elif len(args) == 2:  # Check if attribute name is missing
                print("** attribute name missing **")
            # Check if value for the attribute name doesn't exist
            elif len(args) == 3:
                print("** value missing **")
            else:
                # Set attribute value
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()  # Save changes to the JSON file


if __name__ == '__main__':
    """Only run the following code when this file is not imported."""
    HBNBCommand().cmdloop()  # Start the cmd loop
