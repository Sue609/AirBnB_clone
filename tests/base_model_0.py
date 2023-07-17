#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestSaveMethod(unittest.TestCase):
    def test_save(self):
        bm = BaseModel()
        bm.save()
        self.assertIsNotNone(bm.updated_at)


if __name__ == '__main__':
    unittest.main()
