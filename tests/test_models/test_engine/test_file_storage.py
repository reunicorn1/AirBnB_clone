#!/usr/bin/python3
"""
Unittest for the FileStorage Class
"""

import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models

class Test_instantiation(unittest.TestCase):
    """This class definesunittests for the instantition of FileStorage class"""

    def test_type_path(self):
        """This function tests the type of __file_path attribute"""
        pack = FileStorage()
        self.assertIs(type(pack.FileStorage__file_path), str)


    def test_type_objs(self):
        """This function tests the type of the attribute __objects"""
        pack = FileStorage()
        self.assertIs(type(pack.FileStorage__objects), dict)

    def test_type_storage(self):
        """This function tests the type of the instant storage"""
        self.assertIs(type(models.storage), FileStorage)

class Test_creating_objs(unittest.TestCase):
    """This class creates objects and checks storage instance changes"""

    @classmethod
    def setUpClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage.FileStorage__objects = {}

    def tearDown(self):
        """removes files created and resets the value of __objects"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage.FileStorage__objects = {}

    def test_obj(self):
        """This function tests the contents of __objects and __file_path"""
        self.assertFalse(os.path.exists("file.json"))
        tdy = datetime.datetime.today()
        base = BaseModel(id="123456", created_at=tdy.isoformat(), updated_at=tdy.isoformat())
        objs = models.storage.all()
        self.assertEqual(models.storage.FileStorage__file_path, "file.json")
        self.assertIn("BaseModel.123456", objs)
        self.assertIs(type(objs["BaseModel.123456"]), BaseModel)

    def test_type_all(self):
        """This function tests the type of the return value method all of FileStorage"""
        self.assertIs(type(models.storage.all()), dict)

    def test_all_args(self):
        """This function tests the all method with an argument"""
        with self.assertRaises(TypeError):
            models.storage.all("args")

    def test_all_dict(self):
        """This function tests all method dictionary"""
        base1 = BaseModel()
        base2 = BaseModel()
        base3 = BaseModel()
        objs = models.storage.all()
        self.assertEqual(len(objs), 3)

    def test_new(self):
        """This function tests the mthod new of FileStorage"""
        base = BaseModel()
        models.storage.new(base)
        self.assertIn("BaseModel." + base.id, model.storage.all.keys())

    def test_new_args(self):
        """This function tests the new method with an argument"""
        with self.assertRaises(TypeError):
            models.storage.new()

        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        """This function tests for the save method of FileStorage"""
        base = BaseModel()
        with open("file.json", encoding="utf-8") as f:
            read_data = f.read()
            self.assertIn("BaseModel." + base.id, read_data)

    def test_save_args(self):
        """This function tests the save method with arguments"""
        with self.assertRaises(TypeError):
            models.storage.save("args")

    def test_reloading_without_save(self):
        """This function calls reload() without save()"""
        models.storage.reload()
        objs = models.storage.all()
        self.assertDictEqual({}, objs)

    def test_reload(self):
        """This function tests the reload function"""
        base1 = BaseModel()
        models.storage.new(base)
        models.storage.save()
        models.storage.FileStorage__objects = {}
        models.storage.reload()
        objs = models.storage.all()
        self.assertIn("BaseModel." + base.id, objs)

    def test_reload_args(self):
        """This function tests the method reload with no arguments"""
        with self.assertRaises(TypeError):
            BaseModel().reload("args")



if __name__ == '__main__':
    unittest.main()
