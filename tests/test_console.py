#!/usr/bin/python3
"""
Test module for console.py
"""

import unittest
import os
import sys
import io
from unittest.mock import patch
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from console import HBNBCommand

current_dir = os.getcwd()

root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)


class TestHBNBCommand(unittest.TestCase):
    """
    class TestHBNBCommand to test the project's command line console
    """

    def setUp(self):
        """ test setup"""
        self.console = HBNBCommand()

    def tearDown(self):
        """test tear down """
        self.console = None

    def test_do_create(self):
        """ test instance creation """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.console.onecmd('create BaseModel')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(len(output), 36)

    def test_do_show(self):
        """ test show method """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            obj = BaseModel()
            obj.save()
            self.console.onecmd('show BaseModel {}'.format(obj.id))
            output = mock_stdout.getvalue().strip()

    def test_do_destroy(self):
        """ test destroy """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            obj = BaseModel()
            obj.save()
            self.console.onecmd('destroy BaseModel {}'.format(obj.id))

    def test_do_all(self):
        """ test all command """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            obj1 = BaseModel()
            obj2 = User()
            obj1.save()
            obj2.save()
            self.console.onecmd('all')
            output = mock_stdout.getvalue().strip()

    def test_do_count(self):
        """ test instance counting """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            obj1 = BaseModel()
            obj2 = User()
            obj1.save()
            obj2.save()
            self.console.onecmd('count BaseModel')
            output = mock_stdout.getvalue().strip()

    def test_do_update(self):
        """ test update """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            obj = BaseModel()
            obj.save()
            self.console.onecmd(
                    'update BaseModel {} name "Test"'.format(obj.id)
                )

    def test_prompt(self):
        """ test correct prompt """
        self.assertEqual(self.console.prompt, '(hbnb) ')


if __name__ == '__main__':
    unittest.main()
