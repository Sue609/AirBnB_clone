#!/usr/bin/python3
"""
The console
"""
import cmd
from models.base_model import BaseModel
from models import storage
import models


classes = ('BaseModel',)


class HBNBCommand(cmd.Cmd):
    """
    This is the entry point of the command line interpreter for the AirBnB_clone
    """
    prompt = '(hbnb) '

    def do_create(self, line):
        """
        Creates an instance of BaseModel, saves it as a JSON file and prints the id
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")
            return


    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")


    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()


    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name
        """
        args = line.split(" ")
        obj_list = []
        objects = storage.all()
        try:
            if args[0] != "":
                models.classes[args[0]]
        except (KeyError, NameError):
            print("** class doesn't exist **")
            return
        try:
            for key, val in objects.items():
                obj_list.append(val)
        except:
            pass
        print(obj_list)


    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        storage.reload()
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()


    def do_quit(self, line):
        """
        Exits the AirBnB console
        """
        return True


    def do_EOF(self, line):
        """Handle the end of file command"""
        return True


    def emptyline(self):
        """Empty line does nothing"""
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
