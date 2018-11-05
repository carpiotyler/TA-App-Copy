from typing import Optional

from StorageManager.myStorageManager import AbstractStorageManager as storage

from UserManager.userManager import UserManager
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
        a = user_manager.add(user.username, user.password)

        # then add result contains user
        self.assertEqual(user.__str__(), a)

        # when adding an existing user
        b = user_manager.add(user.username, user.password)

        # then add result contains error
        self.assertEqual("User Already Exists", b)

    def test_view_user(self):
        # given a user
        user = self.user

        # and a user_manager
        user_manager = self.user_manager

        # when looking up a non-existing user
        a = user_manager.view(user.username)

        # then lookup result contains error
        self.assertEqual("No User Available", a)

        # when adding a non-existing user
        b1 = user_manager.add(user.username, user.password)

        # and looking up said user
        b2 = self.user_manager.view(user.username)

        # then add result contains user
        self.assertEqual(user.__str__(), b1)

        # and lookup result contains user
        self.assertEqual(user.__str__(), b2)

        # when looking up all users
        c1 = user_manager.view()

        # then lookup contains user
        self.assertEqual(user.__str__(), c1)

    def test_edit_user(self):
        # given a user
        user = self.user

        # and a user_manager
        user_manager = self.user_manager

        # when editing a non-existing user
        a = user_manager.edit(user.username, "xyz789")

        # then edit result contains error
        self.assertEqual("No User Available", a)

        # when adding a non-existing user
        b1 = user_manager.add(user.username, user.password)

        # and editing said user
        b2 = user_manager.edit(user.username, "xyz789")

        # then add result contains user
        self.assertEqual(user.__str__(), b1)

        # and edit result contains user
        self.assertEqual(User(user.username, "xyz789").__str__(), b2)


    def test_delete_user(self):
        # given a user
        user = self.user

        # and a user_manager
        user_manager = self.user_manager

        # when adding a non-existing user
        a = user_manager.add(user.username, user.password)

        # then add result contains user
        self.assertEqual(user.__str__(), a)

        # when deleting an existing user
        b = user_manager.delete(user.username)

        # then delete result contains user
        self.assertEqual(user.__str__(), b)

        # when deleting a non-existing user
        c = user_manager.delete(user.username)

        # then delete result contains error
        self.assertEqual("No User Available", c)


class MockStorageManager(storage):

    def __init__(self):
        self.users: [User] = []
        self.courses: [Course] = []
        self.sections: [Section] = []

    def set_up(self):
        self.users.append(User("supervisor", "1234", "supervisor"))

    def insert_user(self, user: User):
        self.users.append(user)

    def delete_user(self, user: User):
        self.users.remove(user)

    def get_user(self, username) -> Optional[User]:
        return next(filter(lambda n: (n.username == username), self.users), None)

    def get_all_users(self) -> [User]:
        return self.users

    def insert_course(self, course: Course):
        self.courses.append(course)

    def delete_course(self, course: Course):
        self.courses.remove(course)

    def get_course(self, dept, cnum) -> Optional[Course]:
        return next(filter(lambda n: (n.dept == dept & n.cnum == cnum), self.courses), None)

    def get_all_courses(self) -> [Course]:
        return self.courses

    def get_all_courses_by_dept(self, dept) -> [Course]:
        return filter(lambda n: (n.dept == dept), self.courses)

    def insert_section(self, section: Section):
        self.sections.append(section)

    def delete_section(self, section: Section):
        self.sections.remove(section)

    def get_section(self, dept, cnum, snum) -> Optional[Section]:
        return next(filter(lambda n: (n.dept == dept & n.cnum == cnum & n.snum == snum), self.sections), None)

    def get_all_sections(self) -> [Section]:
        return self.sections

    def get_all_sections_by_dept(self, dept) -> [Section]:
        return filter(lambda n: (n.dept == dept), self.sections)

    def get_all_sections_by_course(self, dept, cnum) -> [Section]:
        return filter(lambda n: (n.dept == dept & n.cnum == cnum), self.sections)