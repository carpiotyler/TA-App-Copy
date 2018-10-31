from StorageManager import JSONStorageManager as jsm
import os, json
from pathlib import Path
import unittest


class JSONStorageManagerTests(unittest.TestCase):

    # unittests for testing JSONStorageManager
    def test_init(self): pass

    def test_set_up(self):
        # Tests that set_up does indeed create a new database, removing as a conditional

        #Deleting any test.json that exists
        try:
            file = open("test.json", "w")
            file.close()
            os.remove("test.json")
        except FileNotFoundError:
            pass

        # Creating new JSON database, and then running set_up (Should create a test.json text file)
        db = jsm.JSONStorageManager("test.json")
        self.assertTrue(db.set_up(False))
        file = Path("test.json")
        self.assertTrue(file.exists(), "File must exist in /StorageManager/ !")

        # Test that new json text file has "courses", "users", and "sections" keys
        file = open("test.json")
        data = json.load(file)
        self.assertIsNotNone(data["courses"], "courses root key must exist!")
        self.assertIsNotNone(data["users"], "users root key must exist!")
        self.assertIsNotNone(data["sections"], "sections root key must exist!")

        # Test that an starter admin account has been created, and that is the ONLY account in the list
        self.assertEqual(len(data["users"]), 1, "More than 1 account in user list!")
        self.assertEqual(data["users"][0]["username"], "supervisor", "base account must have username=supervisor on setup!")
        self.assertEqual(data["users"][0]["password"], "123", "base account must have password=123 on setup!")
        file.close()
        os.remove("test.json")

    def test_insert_course(self): pass

    def test_get_course(self): pass

    def test_insert_user(self): pass

    def test_get_user(self): pass

    def test_insert_section(self): pass

    def test_get_section(self): pass


suite = unittest.TestLoader().loadTestsFromTestCase(JSONStorageManagerTests)
unittest.TextTestRunner(verbosity=2).run(suite)
