#!/usr/bin/python3
"""Defines unittests for console.py."""
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    def test_prompt(self):
        """Test the prompt value."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == "__main__":
    unittest.main()
