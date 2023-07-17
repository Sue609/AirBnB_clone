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
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
}


def parse(line):
    """
    Parse the input line
    """
    c_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)
    if c_braces is None:
        if brackets is None:
            return ([i.strip(",") for i in line.split()])
        else:
            lis = split(line[:brackets.span()[0]])
            ret = [i.strip(",") for i in lis]
            return (ret.append(brackets.group()))
    else:
        lis = split(line[:c_braces.span()[0]])
        return [i.strip(",") for i in lis]


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class that defines the commands
    to be used on AirBnB console
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
        Creates an instance of BaseModel, saves it as a JSON file
        and prints the id
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
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = parse(line)
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
        else:
            print(objects["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        args = parse(line)
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key not in objects:
            print("** no instance found **")
            return
        objects.pop(obj_key)
        storage.save()

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
            obj_list = [str(obj) for key, obj in objects.items()
                        if key.split(".")[0] == class_name]
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
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = parse(line)
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        attribute_value = args[3]
        obj = objects[obj_key]
        if attribute_name in ['id', 'created_at', 'updated_at']:
            return
        attr_type = class_dict[class_name].__dict__[attribute_name]
        try:
            if attr_type is int:
                attribute_value = int(attribute_value)
            elif attr_type is float:
                attribute_value = float(attribute_value)
        except ValueError:
            pass
        setattr(obj, attribute_name, attribute_value)
        obj.save()

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
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
