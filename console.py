#!/usr/bin/env python3
'''Entry point of the command interpreter'''

import re
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand which acts as the console of the AirBNB clone
    which is a command interpreter to manipulate data without visual
    interface.
    """

    cls = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def __init__(self):
        super().__init__()
        self.prompt = '(hbnb) '

    def precmd(self, line):
        """This function intervenes and rewrites the command or simply
        just return it unchanged"""
        cmds = [".all", ".count", ".show", ".destroy", ".update"]
        regx = '(?<=\.)[^(]+|[aA-zZ]+(?=\.)|(?<=\(\"|\(\')[a-z0-9\-]+|(?<=\"|\')\w+|\d+'
        if any(cmd in line for cmd in cmds):
            dict_arg = re.search('\{.+\}', line)
            if dict_arg:
                mtch = re.findall('(?<=\.)[^(]+|[aA-zZ]+(?=\.)|(?<=\(\"|\(\')[a-z0-9\-]+', line)
                mtch[0], mtch[1] = mtch[1], mtch[0]
                return " ".join(mtch) + " " + dict_arg.group()
            match = re.findall(regx, line)
            match[0], match[1] = match[1], match[0]
            return " ".join(match)
        return line

    def emptyline(self):
        pass

    def do_quit(self, _):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, _):
        """End-of-file
        """
        return True

    def do_create(self, line):
        """Creates a new instance of the class provided, save it into
        a JSON file, and prints the id
        """
        line = line.split(" ")
        if not len(line[0]):
            print("** class name missing **")
            return
        elif line[0] not in self.cls:
            print("** class doesn't exist **")
            return
        obj = self.cls[line[0]]()
        storage.save()
        print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class and id values
        """
        line = line.split(" ")
        if not len(line[0]):
            print("** class name missing **")
            return
        elif line[0] not in self.cls:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(line[0], line[1])
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[key])

    def do_destroy(self, line):
        """Deletes an instance based on class name and id
        """
        line = line.split(" ")
        if not len(line[0]):
            print("** class name missing **")
            return
        elif line[0] not in self.cls:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(line[0], line[1])
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        obj_dict.pop(key)
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name
        """
        line = line.split(" ")
        if len(line[0]) and line[0] not in self.cls:
            print("** class doesn't exist **")
            return
        obj_dict = storage.all()
        if not len(line[0]):
            print(list(map(lambda x: str(x), obj_dict.values())))
            return
        cls_list = [str(v) for k, v in obj_dict.items() if line[0] in k]
        print(cls_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attributes
        """
        line = shlex.split(line)
        if not line:
            print("** class name missing **")
            return
        elif line[0] not in self.cls:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(line[0], line[1])
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        if len(line) == 2:
            print("** attribute name missing **")
            return
        if len(line) == 3:
            print("** value missing **")
            return
        if re.search('\{.+:', line[2]) and re.search('.*\}$', line[-1]):
            dict_arg = " ".join(line[2:])
            list_arg = re.findall('[a-zA-Z0-9_-]+', dict_arg)
            for i in range(0, len(list_arg), 2):
                self.updating_obj(key, list_arg[i], list_arg[i + 1])
            return
        self.updating_obj(key, line[2], line[3])

    @staticmethod
    def updating_obj(key, name, value):
        """This function takes care of updating a certain obj with a
        new name and value"""
        obj_dict = storage.all()
        obj = obj_dict[key]
        if hasattr(obj, name):
            type_attr = type(getattr(obj, name))
            value = type_attr(value)
        setattr(obj, name, value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
