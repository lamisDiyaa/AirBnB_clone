#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing the FileStorage class."""

    def test_instantiation(self):
        """Test instantiation of FileStorage."""
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)


if __name__ == "__main__":
    unittest.main()
