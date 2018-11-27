from typing import Optional

from Managers.myStorageManager import AbstractStorageManager as storage

from Managers.userManager import UserManager
from Domain.section import Section
from Domain.course import Course
from Domain.user import User

import unittest


class UserManagerTests(unittest.TestCase):

    def setUp(self):
        self.user = User("foo", "abc123")
        self.user_manager = UserManager(MockStorageManager())

    def tearDown(self):
        del self.user_manager
        del self.user

    def test_user_add(self):
        # given a user
        user = self.user

        # and a user_manager
        user_manager = self.user_manager

        # when adding a non-existing user
        a = user_manager.add({"username": user.username, "password": user.password})

        # then add result contains user
        self.assertTrue(a)

        # when adding an existing user
        b = user_manager.add({"username": user.username, "password": user.password})

        # then add result contains error
        self.assertFalse(b)

    def test_view_user(self):
        # given a user
        user = self.user

        # and a user_manager
        user_manager = self.user_manager

        # when looking up a non-existing user
        a = user_manager.view({"username": user.username})

        # then lookup result contains error
        self.assertEqual("No User Available", a)

        # when adding a non-existing user
        b1 = user_manager.add({"username": user.username, "password": user.password})

        # and looking up said user
        b2 = self.user_manager.view({"username": user.username})

        # then add result contains user
        self.assertTrue(b1)

        # and lookup result contains user
        self.assertEqual(user.__str__(), b2)

        # when looking up all users
        c1 = user_manager.view({})

        # then lookup contains user
        self.assertEqual(user.__str__(), c1)

    def test_edit_user(self):
        # given a user
        user = self.user

        # and a user_manager
        user_manager = self.user_manager

        # when editing a non-existing user
        a = user_manager.edit({"username": user.username, "password": "xyz789"})

        # then edit result contains error
        self.assertFalse(a)

        # when adding a non-existing user
        b1 = user_manager.add({"username": user.username, "password": user.password})

        # and editing said user
        b2 = user_manager.edit({"username": user.username, "password": "xyz789"})

        # then add result contains user
        self.assertTrue(b1)

        # and edit result contains user
        self.assertTrue(b2)

    def test_delete_user(self):
        # given a user
        user = self.user

        # and a user_manager
        user_manager = self.user_manager

        # when adding a non-existing user
        a = user_manager.add({"username": user.username, "password": user.password})

        # then add result contains user
        self.assertTrue(a)

        # when deleting an existing user
        b = user_manager.delete({"username": user.username})

        # then delete result contains user
        self.assertTrue(b)

        # when deleting a non-existing user
        c = user_manager.delete({"username": user.username})

        # then delete result contains error
        self.assertTrue(c) # TODO DELETE METHOD


class MockStorageManager(storage):

    def __init__(self):
        self.users: [User] = []
        self.courses: [Course] = []
        self.sections: [Section] = []

    def set_up(self):
        self.users.append(User("supervisor", "1234", "supervisor"))

    def insert_course(self, course):
        self.courses.append(course)

    def insert_user(self, user):
        self.users.append(user)

    def insert_section(self, section):
        self.sections.append(section)

    def get_course(self, dept, cnum):
        return next(filter(lambda n: (n.dept == dept & n.cnum == cnum), self.courses), [])

    def get_user(self, username):
        if username is "" or None:
            return self.users
        return next(filter(lambda n: (n.username == username), self.users), None)

    def get_section(self, dept, cnum, snum):
        return next(filter(lambda n: (n.dept == dept & n.cnum == cnum & n.snum == snum), self.sections), [])