from StorageManager import JSONStorageManager as jsm
import unittest


class JSONStorageManagerTests(unittest.TestCase):

    # unittests for testing JSONStorageManager

    db = jsm.JSONStorageManager("test.json")

    def test_setUp(self): pass

    def test_insert_course(self): pass

    def test_get_course(self): pass

    def test_insert_user(self): pass

    def test_get_user(self): pass

    def test_insert_section(self): pass

    def test_get_section(self): pass
