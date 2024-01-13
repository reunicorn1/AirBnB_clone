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
        out = 'List available commands with "help" or detailed help with "help cmd".'
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(out, f.getvalue().strip())

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
        out = ["Updates an instance based on the class name and id by adding\n",
               "        or updating attributes"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(''.join(out), f.getvalue().strip())


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
        """This function tests show command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Model"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_create_invalid_method(self):
        """This function tests show command with missing class name"""
        out1 = "*** Unknown syntax: Model.create()"
        out2 = "*** Unknown syntax: User.create()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Model.create()"))
            self.assertEqual(out1, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User,create()"))
            self.assertEqual(out2, f.getvalue().strip())

    def test_create_cmd_basemodel(self):
        """This method creates a new BaseModel"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            obj_id = f.getvalue().strip()
        with open(models.storage._FileStorage__file_path, encoding="utf-8") as file:
            read_data = f.read()
            self.assertIn("BaseModel." + obj_id, read_data)
        self.assertIn("BaseModel." + obj_id, models.storage.all().keys())

    def test_create_cmd_user(self):
        """This method creates a new User"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.create()"))
            obj_id = f.getvalue().strip()
        with open(models.storage._FileStorage__file_path, encoding="utf-8") as file:
            read_data = f.read()
            self.assertIn("User." + obj_id, read_data)
        self.assertIn("User." + obj_id, models.storage.all().keys())

    def test_create_cmd_city(self):
        """this method creates a new city"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertfalse(hbnbcommand().onecmd("City.create()"))
            obj_id = f.getvalue().strip()
        with open(models.storage._filestorage__file_path, encoding="utf-8") as file:
            read_data = f.read()
            self.assertin("City." + obj_id, read_data)
        self.assertin("City." + obj_id, models.storage.all().keys())

    def test_create_cmd_state(self):
        """this method creates a new state"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertfalse(hbnbcommand().onecmd("State.create()"))
            obj_id = f.getvalue().strip()
        with open(models.storage._filestorage__file_path, encoding="utf-8") as file:
            read_data = f.read()
            self.assertin("State." + obj_id, read_data)
        self.assertin("State." + obj_id, models.storage.all().keys())

    def test_create_cmd_amenity(self):
        """this method creates a new amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertfalse(hbnbcommand().onecmd("Amenity.create()"))
            obj_id = f.getvalue().strip()
        with open(models.storage._filestorage__file_path, encoding="utf-8") as file:
            read_data = f.read()
            self.assertin("Amenity." + obj_id, read_data)
        self.assertin("Amenity." + obj_id, models.storage.all().keys())



if __name__ == '__main__':
    unittest.main()
