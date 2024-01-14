#!/usr/bin/python3
"""
Unittest for the console including the class HBNBCommand
"""

import unittest
import models
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole_Base(unittest.TestCase):
    """This class defines unittests for the basic usage of the console"""

    def test_prompt(self):
        """This function tests having the correct prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_quit_return(self):
        """This function tests the return of onecmd function during quitting"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_eof_return(self):
        """This function tests the return of onecmd function during eof"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_invalid_cmd(self):
        """This function tests the output when the class recieves
        invalid cmd"""
        invalid_output = "*** Unknown syntax: arg"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("arg"))
            self.assertEqual(invalid_output, f.getvalue().strip())

    def test_empty_line(self):
        """This function tests recieving an empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

    def test_help(self):
        """This function tests the expected output of the command help"""
        cmds = ['EOF', 'all', 'count', 'create', 'destroy',
                'help', 'quit', 'show', 'update']
        expected = ("Documented commands (type help <topic>):\n",
                    "========================================\n",
                    '  '.join(cmds))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(''.join(expected), f.getvalue().strip())


class TestConsole_help(unittest.TestCase):
    """This class defines unittests for the help method of the console"""

    def test_help_EOF(self):
        """This function tests the <help EOF> message content"""
        expected = "End-of-file"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_all(self):
        """This function tests the <help all> message content"""
        out = ["Prints all string representation of all instances based or\n",
               "        not on the class name"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(''.join(out), f.getvalue().strip())

    def test_help_count(self):
        """This function tests the <help count> message content"""
        out = "Retrives the number of instances of a class"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_create(self):
        """This function tests the <help create> message content"""
        out = ["Creates a new instance of the class provided, save it into\n",
               "        a JSON file, and prints the id"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(''.join(out), f.getvalue().strip())

    def test_help_destroy(self):
        """This function tests the <help destroy> message content"""
        out = "Deletes an instance based on class name and id"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_help(self):
        """This function tests the <help help> message content"""
        out = ['List available commands with "help" or detailed',
               'help with "help cmd".']
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(" ".join(out), f.getvalue().strip())

    def test_help_quit(self):
        """This function tests the <help quit> message content"""
        out = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_show(self):
        """This function tests the <help show> message content"""
        out = ["Prints the string representation of an instance based on\n",
               "        the class and id values"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(''.join(out), f.getvalue().strip())

    def test_help_create(self):
        """This function tests the <help update> message content"""
        o = ["Updates an instance based on the class name and id by adding\n",
             "        or updating attributes"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(''.join(o), f.getvalue().strip())


class TestConsole_create(unittest.TestCase):
    """This class defines unittests for the create method of the console"""

    @classmethod
    def setUpClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def tearDown(self):
        """removes files created and resets the value of __objects"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def test_create_invalid(self):
        """This function tests create command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Model"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())


    def test_create_invalid_method(self):
        """This function tests create command with missing arguments in method format"""
        out1 = "*** Unknown syntax: Model.create()"
        out2 = "*** Unknown syntax: User.create()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Model.create()"))
            self.assertEqual(out1, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.create()"))
            self.assertEqual(out2, f.getvalue().strip())

    def test_create_cmd_basemodel(self):
        """This method creates a new BaseModel"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as file:
            read_data = file.read()
            self.assertIn("BaseModel." + obj_id, read_data)
        self.assertIn("BaseModel." + obj_id, models.storage.all().keys())

    def test_create_cmd_user(self):
        """This method creates a new User"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as file:
            read_data = file.read()
            self.assertIn("User." + obj_id, read_data)
        self.assertIn("User." + obj_id, models.storage.all().keys())

    def test_create_cmd_city(self):
        """this method creates a new city"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as file:
            read_data = file.read()
            self.assertIn("City." + obj_id, read_data)
        self.assertIn("City." + obj_id, models.storage.all().keys())

    def test_create_cmd_state(self):
        """this method creates a new state"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as file:
            read_data = file.read()
            self.assertIn("State." + obj_id, read_data)
        self.assertIn("State." + obj_id, models.storage.all().keys())

    def test_create_cmd_amenity(self):
        """this method creates a new amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as file:
            read_data = file.read()
            self.assertIn("Amenity." + obj_id, read_data)
        self.assertIn("Amenity." + obj_id, models.storage.all().keys())


class TestConsole_create(unittest.TestCase):
    """This class defines unittests for the create method of the console"""

    @classmethod
    def setUpClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def tearDown(self):
        """removes files created and resets the value of __objects"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def test_show_invalid(self):
        """This function tests show command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Model"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Model.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())


    def test_show_instance_id_missing(self):
        """This function tests every possibility of recieving "id missing" msg"""
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())

    def test_show_invalid_id(self):
        """This function tests all the possibilities of recieving an invalid id msg"""
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd('BaseModel.show("1212121")')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd('User.show("1212121")')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())


    def test_show_objs(self):
        """This function tests the functionality of the show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel " + obj_id))
            obj = models.storage.all()["BaseModel." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User " + obj_id))
            obj = models.storage.all()["User." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State " + obj_id))
            obj = models.storage.all()["State." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City " + obj_id))
            obj = models.storage.all()["City." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity " + obj_id))
            obj = models.storage.all()["Amenity." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place " + obj_id))
            obj = models.storage.all()["Place." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review " + obj_id))
            obj = models.storage.all()["Review." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel " + obj_id))
            obj = models.storage.all()["BaseModel." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))

    def test_show_method_format(self):
        """This function tests the show method in the dot notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel,show('{}')".format(obj_id)))
            obj = models.storage.all()["BaseModel." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User,show('{}')".format(obj_id)))
            obj = models.storage.all()["User." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State,show('{}')".format(obj_id)))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["State." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City,show('{}') ".format(obj_id)))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["City." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity,show('{}')".format(obj_id)))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["Amenity." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place,show('{}')".format(obj_id)))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["Place." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.show('{}')".format(obj_id)))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["Review." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))


if __name__ == '__main__':
    unittest.main()
