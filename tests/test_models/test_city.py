#!/usr/bin/python3
"""Test City"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testcity(unittest.TestCase):
    """Test for city"""
    def test_pep8_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """test class"""
        CITY = City()
        self.assertEqual(CITY.__class__.__name__, "City")

    def test_father(self):
        """test inheritance"""
        CITY = City()
        self.assertTrue(issubclass(CITY.__class__, BaseModel))
