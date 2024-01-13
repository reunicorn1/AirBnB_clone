#!/usr/bin/env python3
"""
Unittest for the Class "City"
"""

import unittest
import time
import datetime
from models.city import City
import models


class Test_City(unittest.TestCase):
    """This class defines unittests for the different attributes both inherited
    and unique for the City Class"""

    def test_uniq_time(self):
        """This function tests for the uniquenss of time creation"""
        city1 = City()
        time.sleep(0.001)
        city2 = City()
        self.assertNotEqual(city1.created_at, city2.created_at)

    def test_uniq_id(self):
        """This function tests for the uniqueness of the id"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_custom_id(self):
        """This function creates a City with a specific ID"""
        city = City()
        city.id = "123456"
        self.assertEqual(city.id, "123456")

    def test_type_id(self):
        """This function tests the type of id attr"""
        self.assertIs(type(City().id), str)

    def test_type_created_at(self):
        """This function tests the type of created_at attr"""
        self.assertIs(type(City().created_at), datetime.datetime)

    def test_type_updated_at(self):
        """This function tests for the type of updated_at attr"""
        self.assertIs(type(City().updated_at), datetime.datetime)

    def test_type_state_id(self):
        """This function tests the type of name attr"""
        self.assertIs(type(City().state_id), str)

    def test_type_name(self):
        """This function tests the type of name attr"""
        self.assertIs(type(City().name), str)

    def test_obj_storage(self):
        """This function tests that an object is automatically saved in
        the ___objects attr of storage instance"""
        city = City()
        self.assertIn(city, models.storage.all().values())

    def test_type_class(self):
        """This function tests the type of an instance created"""
        self.assertIs(type(City()), City)

    def test_str(self):
        """This funtion tests string representation of a BaseModel"""
        city = City()
        city.id = "123456"
        tdy = datetime.datetime.today()
        city.created_at = city.updated_at = tdy
        self.assertIn("[City] (123456)", city.__str__())
        self.assertIn("'id': '123456'", city.__str__())
        self.assertIn("'created_at': " + repr(tdy), city.__str__())
        self.assertIn("'updated_at': " + repr(tdy), city.__str__())


class Test_instantation(unittest.TestCase):
    """This class tests the instantation of a City class"""

    def test_init_kwargs(self):
        """This function create a City with kwargs"""
        tdy = datetime.datetime.today()
        city = City(id="123456", created_at=tdy.isoformat(),
                    updated_at=tdy.isoformat(),
                    name="texas", state_id="345")
        self.assertEqual(city.id, "123456")
        self.assertEqual(city.created_at, tdy)
        self.assertEqual(city.updated_at, tdy)
        self.assertEqual(city.name, "texas")
        self.assertEqual(city.state_id, "345")


    def test_init_args(self):
        """This function creates a City without args"""
        tdy = datetime.datetime.today()
        city = City("7890", id="4567", created_at=tdy.isoformat(),
                      updated_at=tdy.isoformat())
        self.assertEqual(city.id, "4567")
        self.assertEqual(city.created_at, tdy)
        self.assertEqual(city.updated_at, tdy)

    def teat_init_class(self):
        """This function tests giving args a class key"""
        city1 = City()
        dict_city1 = city1.to_dict()
        dict_city1['__class__'] = "BaseModel"
        city2 = City(**dict_city1)
        dict_city2 = city2.to_dict()
        self.assertEqual(dict_city2['__class__'], "City")


class Test_save(unittest.TestCase):
    """This class tests the instance method save(self)"""

    def test_save(self):
        """This function tests updating the time"""
        city = City()
        old_time = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, old_time)

    def test_two_save(self):
        """This function tests updates the time twice"""
        city = City()
        first_time = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, first_time)
        second_time = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, second_time)

    def test_save_args(self):
        """This function give save method an argument"""
        with self.assertRaises(TypeError):
            City().save("arg")

    def test_save_file(self):
        """This function tests saving into a JSOM file"""
        city = City()
        city.save()
        with open(models.storage._FileStorage__file_path, encoding="utf-8") as f:
            self.assertIn("City." + city.id, f.read())


class Test_to_dict(unittest.TestCase):
    """unittests for the instance method to_dict"""

    def test_type_dict(self):
        """This function tests the type of to_dict return value"""
        self.assertIs(type(City().to_dict()), dict)

    def test_contents_dict(self):
        """This function tests the contents of a dictionary"""
        city = City()
        self.assertIn('updated_at', city.to_dict())
        self.assertIn('__class__', city.to_dict())
        self.assertIn('id', city.to_dict())
        self.assertIn('created_at', city.to_dict())

    def test_dynamic_dict(self):
        """This function tests the dynamic creation of attributes in dict"""
        city = City()
        city.country = "US"
        city.postal_code = 456
        self.assertIn('country', city.to_dict())
        self.assertIn('postal_code', city.to_dict())

    def test_type_time_in_dict(self):
        """This function tests the type of created_at and updated_at in dict"""
        city = City()
        city_dict = city.to_dict()
        self.assertIs(type(city_dict['created_at']), str)
        self.assertIs(type(city_dict['updated_at']), str)

    def test_dict_kwargs(self):
        """This function create a User with kwargs and tests its dict"""
        tdy = datetime.datetime.today()
        city = City(id="123456", created_at=tdy.isoformat(),
                   updated_at=tdy.isoformat(), name="florida")
        city_dict = city.to_dict()
        self.assertIn('name', city_dict)

    def test_full_dict(self):
        """This function tests creation of a dictionary"""
        city = City()
        city.id = "123456"
        tdy = datetime.datetime.today()
        city.created_at = city.updated_at = tdy
        dict_city = {'__class__': 'City',
                      'updated_at': tdy.isoformat(),
                      'created_at': tdy.isoformat(),
                      'id': "123456"}
        self.assertDictEqual(city.to_dict(), dict_city)

    def test_dict_class(self):
        """This function tests that __dict__ repr and to_dict()
        are different"""
        city = City()
        self.assertNotEqual(city.__dict__, city.to_dict())

    def test_to_dict_arg(self):
        """This function tests giving the instance method to_dict arguments"""
        with self.assertRaises(TypeError):
            City().to_dict("arg")


if __name__ == '__main__':
    unittest.main()
