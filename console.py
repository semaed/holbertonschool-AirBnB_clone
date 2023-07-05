#!/usr/bin/env python3
""" Module for the entry point of the
command inerpreter"""
# Import cmd for command line interpreters.
import cmd


# Class for our command interpreter.
class HBNBCommand(cmd.Cmd):

    # Set the prompt for the console.
    prompt = '(hbnb) '

    # Command 'quit' to exit the program.
    def do_quit(self, args):
        """Exits the program."""
        # If the 'quit' command is executed, the command loop ends.
        raise SystemExit

    # Command 'EOF' to exit the program.
    def do_EOF(self, args):
        """Also exits the program."""
        # If the 'EOF' command is executed, the command loop ends.
        raise SystemExit

    # If line is empty, do nothing.
    def emptyline(self):
        """Do nothing if line is empty."""
        # If an empty line is entered, do nothing.
        pass


# Run command loop if file is run directly.
if __name__ == '__main__':
    """Run only if called directly."""
    HBNBCommand().cmdloop()
