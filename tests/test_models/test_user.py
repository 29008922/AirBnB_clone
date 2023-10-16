#!/usr/bin/python3
"""Test User"""
import unittest
import pep8
from models.user import User


class Testuser(unittest.TestCase):
    """Test User"""

    def test_pep8_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_User(self):
        """
        Test attributes of Class Use
        """
        myUser = User()
        myUser.first_name = 'Holberton'
        myUser.last_name = 'School'
        myUser.email = '2020@holbertonschool.com'
        self.assertEqual(myUser.first_name, 'Holberton')
        self.assertEqual(myUser.last_name, 'School')
        self.assertEqual(myUser.email, '2020@holbertonschool.com')
