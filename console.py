#!/usr/bin/python3
"""
The console module: 
    HBNBClass to be used in AirBnB console
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_dict = {
        "BaseModel": BaseModel,
        "User": User,
}


classes = ('BaseModel',)


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class that defines the commands to be used on AirBnB console
    It access and modifies the web app's data
    """
    prompt = '(hbnb) '


    def default(self, line):
        """
        Default behavior for cmd module when input is invalid
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        match = re.search(r"\.", line)
        if match is not None:
            argl = [line[:match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(line))
        return False


    def do_create(self, line):
        """
        Creates an instance of BaseModel, saves it as a JSON file and prints the id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name in class_dict:
            new_instance = class_dict[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")


    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        """
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        key = class_name + "." + obj_id
        objects = storage.all()
        if key in objects:
            obj = objects[key]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """

        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        key = class_name + "." + obj_id
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")


    def do_all(self, line):
        """
        Prints all string representation of all instances 
        based or not on the class name
        """

        args = line.split()
        objects = storage.all()
        if len(args) == 0:
            obj_list = [str(obj) for obj in objects.values()]
        elif args[0] in class_dict:
            class_name = args[0]
            obj_list = [str(obj) for key, obj in objects.items() if key.split(".")[0] == class_name]
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)


    def do_count(self, line):
        """
        Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        argl = line.split()
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """

        args = lene.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        key = class_name + "." + obj_id
        objects = storage.all()
        if key in objects:
            obj = objects[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            value = args[3]
            setattr(obj, attribute_name, value)
            storage.save()
        else:
            print("** no instance found **")
        

    def do_quit(self, line):
        """
        Exits the AirBnB console
        """
        return True


    def do_EOF(self, line):
        """
        Handle the end of file command (exits console)
        """
        print()
        return True


    def emptyline(self):
        """
        Empty line does nothing
        """
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
