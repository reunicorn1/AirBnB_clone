#!/usr/bin/env python3
'''Entry point of the command interpreter'''

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand which acts as the console of the AirBNB clone
    which is a command interpreter to manipulate data without visual
    interface.
    """

    cls = {"BaseModel": BaseModel}

    def __init__(self):
        super().__init__()
        self.prompt = '(hbnb) '

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
        """Prints the string representation of an instance based on the class
        and id values
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
        """Prints all string representation of all instances based or not on
        the class name
        """
        line = line.split(" ")
        if len(line[0]) and line[0] not in self.cls:
            print("** class doesn't exist **")
            return
        obj_dict = storage.all()
        if not len(line[0]):
            print(list(map(lambda x: str(x), obj_dict.values())))
            return
        cls_list = [str(val) for key, val in obj_dict.items() if line[0] in key]
        print(cls_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating
        attributes
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
        obj = obj_dict[key]
        if hasattr(obj, line[2]):
            type_attr = type(getattr(obj, line[2]))
            line[3] = type_attr(line[3])
        setattr(obj, line[2], line[3])




if __name__ == '__main__':
    HBNBCommand().cmdloop()
