#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    def test_instantiation(self):
        """Test instantiation of BaseModel."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)


if __name__ == "__main__":
    unittest.main()
