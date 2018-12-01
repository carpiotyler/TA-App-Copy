from Managers.DjangoStorageManager import DjangoStorageManager as dm
from TAServer.models import Course, Section, Staff as User
from Managers.userManager import UserManager
from django.test import TestCase


class UserManagerTests(TestCase):

    def setUp(self):
        self.user_manager = UserManager(dm)

    def tearDown(self):
        del self.user_manager

    def test_user_add_basic(self):
        # Basic fields case
        fields = {'username':'test',
                  'password':'123'}

        # Testing that the returns are the expected behavior:
        self.assertTrue(self.user_manager.add(self, fields), "Should be a valid user add!")
        self.assertFalse(self.user_manager.add(self, fields), "Should no longer be able to add !: User Exists")

    def test_user_add_incorrect_fields(self):
        # Completely incorrect add, the req fields aren't filled out!
        fields = {'un': 'new',
                  'pass': 'lola'}
        self.assertFalse(self.user_manager.add(self, fields), "Should only add if reqfields are filled out!")

    def test_user_add_complicated(self):
        # A complicated, highest level test, shouldn't fail or throw exceptions:
        fields = {'username': 'test',
                  'password': '123',
                  'role': User.ROLES["I"],  # Instructor, ins, whatever
                  'email':'foo@bar.com',
                  'address':'123 sesame street'}

        # Return val checking for subsequent calls
        self.assertTrue(self.user_manager.add(self, fields), "Failed on omplicated user add")
        self.assertFalse(self.user_manager.add(self, fields, "Shouldn't be able to call again"))

    def test_view_user_basic(self):
        # adding basic user to test with
        fields = {'username': 'test',
                  'password': '123'}

        self.assertEqual(self.user_manager.view({"username":"test"}), "No Users", "No users case!")
        self.assertTrue(self.user_manager.add(self, fields))
        self.assertEqual(self.user_manager.view(self, fields), "test\nrole=default\n\n")

    def test_view_user_all_basic(self):
        # Adding three basic users to test with
        fields1 = {'username': 'test',
                  'password': '123'}

        fields2 = {'username': 'scotty',
                  'password': '232',
                   'role':User.ROLES["A"]}

        fields3 = {'username': 'truff',
                  'password': 'pass',
                   'role':User.ROLES["I"]}

        self.assertTrue(self.user_manager.add(self, fields1), "Error adding fields1!")
        self.assertTrue(self.user_manager.add(self, fields2), "Error adding fields2!")
        self.assertTrue(self.user_manager.add(self, fields3), "Error adding fields3!")

        # View all (no username or role provided) must return all users, alphabetically sorted by username
        self.assertEqual(self.user_manager.view(self, {}),
                "scotty\nrole=administrator\n\nsup\nrole=supervisor\n\ntest\nrole=default\n\ntruff\nrole=instructor\n\n"
                , "This is a long, convoluted sting, but this is the expected output")

    def test_edit_user_basic(self):
        # Basic fields case
        fields = {'username': 'test',
                  'password': '123'}

        self.assertFalse(self.user_manager.edit(self, fields, "No user to edit!"))
        self.assertTrue(self.user_manager.add(self, fields), "Add should work")
        # Editing nothing should still return true
        self.assertTrue(self.user_manager.edit(self, fields), "Edit should return true if user exists! Even if no changes!")
        # Basic editing
        # Basic fields case
        fields = {'username': 'test',
                  'password': 'newpass'}
        self.assertTrue(self.user_manager.edit(self, fields), "Edit should return true.")

    def test_edit_user_roles_and_view_integrated(self):
        # Basic fields case
        fields = {'username': 'test',
                  'password': '123'}

        self.assertTrue(self.user_manager.add(self, fields))
        self.assertEqual(self.user_manager.view(self, {"username":"test"}), "test\nrole=default")
        # Basic fields case
        fields = {'username': 'test',
                  'password': '123',
                  'role': User.ROLES['I']}
        self.assertTrue(self.user_manager.edit(self, fields))
        self.assertEqual(self.user_manager.view(self,{"username":"test"}), "test\nrole=instructor", "Edited!")

    def test_delete_user(self):
        # Basic fields case
        fields = {'username': 'test',
                  'password': '123'}
        self.assertTrue(self.user_manager.add(fields))
        self.assertEqual(self.user_manager.view(self, {"username":"test"}), "test\nrole=default")
        self.assertTrue(self.user_manager.delete(self, {"username":"test"}))
        self.assertEqual(self.user_manager.view(self, {"username":"test"}), "No Users", "Should have been deleted!")
