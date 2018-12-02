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
        self.assertTrue(self.user_manager.add(fields), "Should be a valid user add!")
        self.assertFalse(self.user_manager.add(fields), "Should no longer be able to add !: User Exists")

    def test_user_add_incorrect_fields(self):
        # Completely incorrect add, the req fields aren't filled out!
        fields = {'un': 'new',
                  'pass': 'lola'}
        self.assertFalse(self.user_manager.add(fields), "Should only add if reqfields are filled out!")

        fields = {'username': 'test',
                  'password':'123',
                  'role': 'student'}
        self.assertFalse(self.user_manager.add(fields), "Role provided not in ROLES! Should not add!")

    def test_user_add_complicated(self):
        # A complicated, highest level test, shouldn't fail or throw exceptions:
        fields = {'username': 'test',
                  'password': '123',
                  'role': dict(User.ROLES)["I"],  # Instructor, ins, whatever
                  'email':'foo@bar.com',
                  'address':'123 sesame street'}

        # Return val checking for subsequent calls
        self.assertTrue(self.user_manager.add(fields), "Failed on omplicated user add")
        self.assertFalse(self.user_manager.add(fields), "Shouldn't be able to call again")

    def test_view_user_basic(self):
        # adding basic user to test with
        fields = {'username': 'test',
                  'password': '123'}

        self.assertEqual(self.user_manager.view({"username":"test"}), "no users", "No users case!")
        self.assertTrue(self.user_manager.add(fields))
        self.assertEqual(self.user_manager.view(fields), "test\nrole=default\n\n")

    def test_view_user_all_basic(self):
        # Adding three basic users to test with
        fields1 = {'username': 'test',
                  'password': '123'}

        fields2 = {'username': 'scotty',
                  'password': '232',
                   'role':dict(User.ROLES)["A"]}

        fields3 = {'username': 'truff',
                  'password': 'pass',
                   'role':dict(User.ROLES)["I"]}

        self.assertTrue(self.user_manager.add(fields1), "Error adding fields1!")
        self.assertTrue(self.user_manager.add(fields2), "Error adding fields2!")
        self.assertTrue(self.user_manager.add(fields3), "Error adding fields3!")

        # View all (no username or role provided) must return all users, alphabetically sorted by username
        self.assertEqual(self.user_manager.view({}),
                "scotty\nrole=administrator\n\nsupervisor\nrole=supervisor\n\ntest\nrole=default\n\ntruff\nrole=instructor\n\n"
                , "This is a long, convoluted sting, but this is the expected output")

    def test_edit_user_basic(self):
        # Basic fields case
        fields = {'username': 'test',
                  'password': '123'}

        self.assertFalse(self.user_manager.edit(fields), "No user to edit!")
        self.assertTrue(self.user_manager.add(fields), "Add should work")
        # Editing nothing should still return true
        self.assertTrue(self.user_manager.edit(fields), "Edit should return true if user exists! Even if no changes!")
        # Basic editing
        # Basic fields case
        fields = {'username': 'test',
                  'password': 'newpass'}
        self.assertTrue(self.user_manager.edit(fields), "Edit should return true.")

    def test_edit_user_roles_and_view_integrated(self):
        # Basic fields case
        fields = {'username': 'test',
                  'password': '123'}

        self.assertTrue(self.user_manager.add(fields))
        self.assertEqual(self.user_manager.view({"username":"test"}), "test\nrole=default\n\n")
        # Basic fields case
        fields = {'username': 'test',
                  'password': '123',
                  'role': dict(User.ROLES)['I']}
        self.assertTrue(self.user_manager.edit(fields))
        self.assertEqual(self.user_manager.view({"username":"test"}), "test\nrole=instructor\n\n", "Edited!")

    def test_delete_user(self):
        # Basic fields case
        fields = {'username': 'test',
                  'password': '123'}
        self.assertTrue(self.user_manager.add(fields))
        self.assertEqual(self.user_manager.view({"username":"test"}), "test\nrole=default\n\n")
        self.assertTrue(self.user_manager.delete({"username":"test"}))
        self.assertEqual(self.user_manager.view({"username":"test"}), "no users", "Should have been deleted!")
