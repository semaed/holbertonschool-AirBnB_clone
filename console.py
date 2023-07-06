#!/usr/bin/env python3
""" Module for the entry point of the
command inerpreter"""
# Import cmd for command line interpreters.
import cmd
import shlex
import models
import sys
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
    def do_quit(self, line):
        """Quit command to exit the program"""
        # checks if running in non-interactive mode
        if not sys.stdin.isatty():
            # Prints a newline character.
            print()
        # If the 'quit' command is executed, the command loop ends.
        return True

    # Command 'EOF' to exit the program.
    def do_EOF(self, line):
        """EOF command to exit the program"""
        # exits the cmd loop the same way 'quit' does
        return self.do_quit(line)

    # If line is empty, do nothing.
    def emptyline(self):
        """Do nothing if line is empty."""
        # If an empty line is entered, do nothing.
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""

        # Split the 'arg' into a list by spaces
        args = shlex.split(arg)

        # Check if any arguments were passed, if not, print error and exit
        if len(args) == 0:
            print("** class name missing **")
            return
        
        class_name  = args[0]
        if class_name in storage.classes:
            print("class doesn't exist **")
            return
        
        # Create a new instance of the specified class
        new_instance = storage.classes[class_name]()

        # Save the new instance to a file
        new_instance.save()

        # Print the id of the new instance
        print(new_instance.id)

    def do_show(self, arg):
        """Print string representation of instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        
        if len (args) < 2:
            print("** instance id misiing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("**no instance found **")
            return
        """ Print the string representation of the instance"""
        print(storage.all()[key])
    
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
            return
        # Check if the class name does not exist.
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        # Check if id is missing.
        elif len(args) == 1:
            print("** instance id missing **")
            return

        # Create the key with class name and id.
        key = args[0] + "." + args[1]

        # Check if instance exists.
        if key not in storage.all():
            print("** no instance found **")
            return

        # Check if attribute name is provided.
        elif len(args) == 2:
            print("** attribute name missing **")
            return

        # Check if value for attribute name is missing.
        elif len(args) == 3:
            print("** value missing **")
            return

        else:
            # Get the instance from storage.
            instance = storage.all()[key]
            # Update the attribute with the provided value.
            obj = models.storage.all()[key]
            try:
                attr_type = type(getattr(instance, args[2]))
            except AttributeError:
                pass
            setattr(instance, args[2], args[3])
            instance.save()


# Run command loop if file is run directly.
if __name__ == '__main__':
    """Run only if called directly."""
    HBNBCommand().cmdloop()