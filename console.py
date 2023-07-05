#!/usr/bin/env python3
# Import cmd for command line interpreters.
import cmd

# Class for our command interpreter.


class HBNBCommand(cmd.Cmd):

    # Our prompt will be '(hbnb) '
    prompt = '(hbnb) '

    # Command 'quit' to exit the program.
    def do_quit(self, args):
        """Exits the program."""
        raise SystemExit

    # Command 'EOF' to exit the program.
    def do_EOF(self, args):
        """Also exits the program."""
        raise SystemExit

    # If line is empty, do nothing.
    def emptyline(self):
        """Do nothing if line is empty."""
        pass


# Run command loop if file is run directly.
if __name__ == '__main__':
    """Run only if called directly."""
    HBNBCommand().cmdloop()
