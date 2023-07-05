#!/usr/bin/env python3
""" Module for the entry point of the
command inerpreter"""
# Import cmd for command line interpreters.
import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel


# Create a dictionary of available classes.
classes = {"BaseModel": BaseModel}


# Class for our command interpreter.
class HBNBCommand(cmd.Cmd):

    # Set the prompt for the console.
    prompt = '(hbnb) '

    # Define available classes.
    def __init__(self):
        super(HBNBCommand, self).__init__()
        self.classes = {"BaseModel": BaseModel}

    # Command 'quit' to exit the program.
    def do_quit(self, args):
        """Exits the program."""
        # If the 'quit' command is executed, the command loop ends.
        return True

    # Command 'EOF' to exit the program.
    def do_EOF(self, args):
        """Also exits the program."""
        # If the 'EOF' command is executed, the command loop ends.
        return True

    # If line is empty, do nothing.
    def emptyline(self):
        """Do nothing if line is empty."""
        # If an empty line is entered, do nothing.
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        # If no argument is provided, print an error message.
        if not arg:
            print("** class name missing **")
        # If the class name doesn't exist, print an error message.
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            # Create a new instance of the class.
            new_instance = classes[arg]()
            # Save the new instance.
            new_instance.save()
            # Print the id of the new instance.
            print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of instance"""
        args = arg.split()
        # Check if class name is provided.
        if len(args) == 0:
            print("** class name missing **")
        # Check if class name exists.
        elif args[0] not in classes:
            print("** class doesn't exist **")
        # Check if id is provided.
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Create the key with class name and id.
            key = args[0] + "." + args[1]
            # Check if instance exists.
            if key in storage.all():
                # If instance exists, print it.
                print(storage.all()[key])
            else:
                # If instance does not exist, print error message.
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        # Check if class name is provided.
        if len(args) == 0:
            print("** class name missing **")
        # Check if class name exists.
        elif args[0] not in classes:
            print("** class doesn't exist **")
        # Check if id is provided.
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Create the key with class name and id.
            key = args[0] + "." + args[1]
            # Check if instance exists.
            if key in storage.all():
                # If instance exists, delete it.
                del storage.all()[key]
                # Save the changes.
                storage.save()
            else:
                # If instance does not exist, print error message.
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg not in classes and arg != "":
            # If class name doesn't exist, print an error.
            print("** class doesn't exist **")
        else:
            # Print all instances of the class.
            print([str(v) for k, v in storage.all().items()])

    def do_update(self, arg):
        """Updates an instance."""

        # Split args by spaces into a list
        args = shlex.split(arg)

        # Check for missing arguments
        if len(args) == 0:
            print("** class name missing **")
        # Check if the class name does not exist.
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        # Check if id is missing.
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Create key for objects dict
            key = args[0] + '.' + args[1]

            # Check if key doesn't exist in storage
            if key not in models.storage.all():
                print("** no instance found **")
            # Check if attribute name is missing.
            elif len(args) == 2:
                print("** attribute name missing **")
            # Check if value for attribute name is missing.
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = models.storage.all()[key]
                try:
                    attr_type = type(getattr(obj, args[2]))
                except AttributeError:
                    attr_type = str
                setattr(obj, args[2], attr_type(args[3]))
                obj.save()


# Run command loop if file is run directly.
if __name__ == '__main__':
    """Run only if called directly."""
    HBNBCommand().cmdloop()
