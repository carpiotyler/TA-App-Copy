from StorageManager import JSONStorageManager as jsm

import os, json
from pathlib import Path
import unittest


class JSONStorageManagerTests(unittest.TestCase):

    # unittests for testing JSONStorageManager

    # Deleting any test.json that exists

    def setUp(self):
        # In case before testing a tes.json somehow exists
        try:
            self.file = open("test.json", "w")
        except FileNotFoundError:
            pass
        self.file.close()
        os.remove("test.json")
        self.db = jsm.JSONStorageManager("test.json")
        self.file = None

    def tearDown(self):
        # To remove file (in case of crashes and such during runs before tests do it
        try:
            self.file = open("test.json", "w")
        except FileNotFoundError:
            pass
        self.file.close()
        os.remove("test.json")

    def test_init(self):
        test_db = jsm.JSONStorageManager()
        self.assertEqual(test_db.file_name, "database.json", "Default json should be database.json!")
        test_db = jsm.JSONStorageManager("random.json")
        self.assertEqual(test_db.file_name, "random.json", "file_name should be what we passed!")

    def test_set_up_json_exists(self):
        # Tests that set_up does indeed create a new database
        # Creating new JSON database, and then running set_up (Should create a test.json text file)
        self.assertTrue(self.db.set_up())
        path = Path("test.json")
        self.assertTrue(path.exists(), "File must exist in /StorageManager/ !")
        os.remove("test.json")

    def test_set_up_basics(self):
        # Test that new json text file has "courses", "users", and "sections" keys
        self.db.set_up()
        self.file = open("test.json")
        data = json.load(self.file)
        self.assertIsNotNone(data["courses"], "courses root key must exist!")
        self.assertIsNotNone(data["users"], "users root key must exist!")
        self.assertIsNotNone(data["sections"], "sections root key must exist!")
        self.file.close()
        os.remove("test.json")

    def test_set_up_starter_account_exists(self):
        # Test that an starter admin account has been created, and that is the ONLY account in the list
        self.db.set_up()
        self.file = open("test.json")
        data = json.load(self.file)
        self.assertEqual(len(data["users"]), 1, "More than 1 account in user list!")
        self.assertEqual(data["users"][0]["username"], "supervisor", "base account must have username=supervisor on setup!")
        self.assertEqual(data["users"][0]["password"], "123", "base account must have password=123 on setup!")
        self.file.close()
        os.remove("test.json")

    def test_insert_course(self):
        # Again, we don't validate incoming data, we just insert the incoming course object to the json database
        self.db.set_up()
        test_course1 = jsm.JSONStorageManager.Course("CS", "351")
        self.db.insert_course(test_course1)
        response_course = self.db.get_course("CS", "351")
        self.assertIsNotNone(response_course)
        self.assertTrue(isinstance(response_course, jsm.JSONStorageManager.Course))
        self.assertEqual(response_course.dept, "CS")
        self.assertEqual(response_course.cnum, "351")
        self.assertIsNotNone(response_course.sections)
        self.assertTrue(isinstance(response_course.sections, list), "sections parameter of any returned course must be a list")

        # Testing inserting a non course object, shouldn't cause a runtime exception
        try:
            self.db.insert_course("351")
        except:
            self.assertTrue(False, "Must not throw an exception! Insert simply ignores all non Course objects!")
        os.remove("test.json")

    def test_insert_course_edit(self):
        # Tests both the "edit" functionality of insert and also tests the section list for usability
        self.db.set_up()
        test_course1 = jsm.JSONStorageManager.Course("CS", "351")
        self.db.insert_course(test_course1)
        test_course1.name = "Data Structures and Algorithms"
        test_course1.sections = ["401", "801", "802"]
        self.db.insert_course(test_course1)
        response_course = self.db.get_course("CS", "351")
        self.assertIsNotNone(response_course)
        self.assertEquals(response_course.name, "Data Structures and Algorithms")
        self.assertEqual(len(response_course.sections), 3)
        self.assertTrue("401" in response_course.sections)
        self.assertTrue("801" in response_course.sections)
        self.assertTrue("802" in response_course.sections)
        os.remove("test.json")

    def test_get_course(self):
        # Tests basic functionality of get_course. Get out what we put in.
        self.file = open("test.json", "w")
        str_test_db = """
            {
                "courses": [
                    {
                        "dept" : "CS",
                        "cnum" : "351",
                        "sections" : ["401"],
                        "name" : "",
                        "description" : ""
                    }
                ],
                "users": [
                    {
                        "username" : "JTB",
                        "password" : "andrew"
                    }
                ],
                "sections": [
                    {
                        "dept": "CS",
                        "cnum": "351",
                        "snum": "401",
                        "instructor" : ""
                    }
                ]
            }
        """
        test_json = json.loads(str_test_db)
        json.dump(test_json, self.file)
        self.file.close()
        response_course = self.db.get_course("CS", "351")
        self.assertIsNotNone(response_course, "Response shouldn't be none!")
        self.assertEqual(response_course.dept, "CS")
        self.assertEqual(response_course.cnum, "351")
        self.assertTrue("401" in response_course.sections)
        # Testing on nonexistent courses
        none_course = self.db.get_course("MATH", "240")
        self.assertIsNone(none_course, "Shouldn't be in database!")

    def test_get_course_all(self):
        # Testing get_course with no dept or cnum (Get all courses)
        self.file = open("test.json", "w")
        str_test_db = """
            {
                "courses": [
                    {
                        "dept" : "CS",
                        "cnum" : "351",
                        "sections" : ["401"],
                        "name" : "",
                        "description" : ""
                    },
                    {
                        "dept" : "MATH",
                        "cnum" : "240",
                        "sections" : ["401"],
                        "name" : "",
                        "description" : ""
                    }
                ],
                "users": [
                    {
                        "username" : "JTB",
                        "password" : "andrew",
                        "role" : ""
                    }
                ],
                "sections": [
                    {
                        "dept": "CS",
                        "cnum": "351",
                        "snum": "401",
                        "instructor" : ""
                    }
                ]
            }
        """
        test_json = json.loads(str_test_db)
        json.dump(test_json, self.file)
        self.file.close()
        all_courses = self.db.get_course()
        self.assertIsNotNone(all_courses)
        self.assertTrue(isinstance(all_courses, list))
        self.assertTrue(len(all_courses), 2)

    def test_get_course_just_dept(self):
        # Testing that get_course called with just a dept returns all courses with that dept
        self.file = open("test.json", "w")
        str_test_db = """
            {
                "courses": [
                    {
                        "dept" : "CS",
                        "cnum" : "351",
                        "sections" : ["401"],
                        "name" : "",
                        "description" : ""
                    },
                    {
                        "dept" : "MATH",
                        "cnum" : "240",
                        "sections" : ["401"],
                        "name" : "",
                        "description" : ""
                    },
                    {
                        "dept" : "CS",
                        "cnum" : "361",
                        "sections" : ["401"],
                        "name" : "",
                        "description" : ""
                    },
                    {
                        "dept" : "CS",
                        "cnum" : "317",
                        "sections" : ["401"],
                        "name" : "",
                        "description" : ""
                    }
                ],
                "users": [
                    {
                        "username" : "JTB",
                        "password" : "andrew",
                        "role" : ""
                    }
                ],
                "sections": [
                    {
                        "dept": "CS",
                        "cnum": "351",
                        "snum": "401",
                        "instructor" : ""
                    }
                ]
            }
        """
        test_json = json.loads(str_test_db)
        json.dump(test_json, self.file)
        self.file.close()
        all_courses = self.db.get_course("CS")
        self.assertIsNotNone(all_courses)
        self.assertTrue(isinstance(all_courses, list))
        self.assertTrue(len(all_courses), 3)
        # Testing on nonexistent depts
        none_course = self.db.get_course("LING")
        self.assertIsNone(none_course, "Shouldn't be in database!")

    def test_insert_user(self):
        # Again, we don't validate incoming data, we just insert the incoming user object to the json database
        self.db.set_up()
        test_user1 = jsm.JSONStorageManager.User("rock", "password")
        self.db.insert_user(test_user1)
        response_user = self.db.get_user("rock")
        self.assertIsNotNone(response_user)
        self.assertTrue(isinstance(response_user, jsm.JSONStorageManager.User))
        self.assertEqual(response_user.username, "rock")
        self.assertEqual(response_user.password, "password")
        self.assertEqual(response_user.role, "")

        # Testing inserting a non user object, shouldn't cause a runtime exception
        try:
            self.db.insert_user("rock")
        except:
            self.assertTrue(False, "Must not throw an exception! Insert simply ignores all non User objects!")
        os.remove("test.json")

    def test_insert_user_edit(self):
        # Tests the "edit" functionality of insert_user
        self.db.set_up()
        test_user1 = jsm.JSONStorageManager.User("rock", "password")
        self.db.insert_user(test_user1)
        test_user1.password = "123"
        test_user1.role = "admin"
        self.db.insert_user(test_user1)
        response_user = self.db.get_user("rock")
        self.assertIsNotNone(response_user)
        self.assertEqual(response_user.username, "rock")
        self.assertEqual(response_user.password, "123")
        self.assertEqual(response_user.role, "admin")
        os.remove("test.json")

    def test_get_user(self):
        # Tests basic functionality of get_user. Get out what we put in.
        self.file = open("test.json", "w")
        str_test_db = """
            {
                "courses": [
                    {
                        "dept" : "CS",
                        "cnum" : "351",
                        "sections" : ["401"],
                        "name" : "",
                        "description" : ""
                    }
                ],
                "users": [
                    {
                        "username" : "JTB",
                        "password" : "andrew",
                        "role" : ""
                    }
                ],
                "sections": [
                    {
                        "dept": "CS",
                        "cnum": "351",
                        "snum": "401",
                        "instructor" : ""
                    }
                ]
            }
        """
        test_json = json.loads(str_test_db)
        json.dump(test_json, self.file)
        self.file.close()
        response_user = self.db.get_user("JTB")
        self.assertIsNotNone(response_user, "Response shouldn't be none!")
        self.assertEqual(response_user.username, "JTB")
        self.assertEqual(response_user.password, "andrew")
        self.assertEqual(response_user.role, "")

        # Testing on nonexistent user
        none_course = self.db.get_user("rock")
        self.assertIsNone(none_course, "Shouldn't be in database!")

    def test_insert_section(self): pass

    def test_insert_section_edit(self): pass

    def test_get_section(self): pass


suite = unittest.TestLoader().loadTestsFromTestCase(JSONStorageManagerTests)
unittest.TextTestRunner(verbosity=2).run(suite)
