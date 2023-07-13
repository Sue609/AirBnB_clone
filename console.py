#!/usr/bin/python3
"""
The console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This is the entry point of the command line interpreter for the AirBnB_clone
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


    def do_EOF(self, line):
        """Handle the end of file command"""
        return True


    def emptyline(self):
        """Empty line does nothing"""
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
