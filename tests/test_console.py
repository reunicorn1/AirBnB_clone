#!/usr/bin/python3
"""
Unittest for the console including the class HBNBCommand
"""

import unittest
import models
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole_Base(unittest.TestCase):
    """This class defines unittests for the basic usage of the console"""

    def test_prompt(self):
        """This function tests having the correct prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand().prompt)

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


if __name__ == '__main__':
    unittest.main()
