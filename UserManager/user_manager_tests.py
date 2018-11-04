from StorageManager.myStorageManager import AbstractStorageManager as storage

from UserManager.user_manager import UserManager
from Domain.section import Section
from Domain.course import Course
from Domain.user import User

import unittest


class UserManagerTests(unittest.TestCase):

    def setUp(self):
        self.userManager = UserManager(MockStorageManager())

    def tearDown(self):
        del self.userManager

    def test_user_add(self):
        user = User("foo", "abc123")
        self.assertEqual(0, self.userManager.view())
        self.userManager.add(user)
        pass

    def test_delete_user(self):
        user = User("foo", "abc123")
        self.userManager.delete(user)
        pass

    def test_edit_user(self):
        user = User("foo", "abc123")
        self.userManager.edit(user)
        pass

    def test_view_user(self):
        user = User("foo", "abc123")
        self.userManager.view(user)
        pass


class MockStorageManager(storage):

    def __init__(self):
        self.users = {}
        self.courses = {}
        self.sections = {}

    def set_up(self):
        pass

    def insert_course(self, course: Course):
        self.courses[course.name] = course
        pass

    def insert_user(self, user: User):
        self.users[user.username] = user
        pass

    def insert_section(self, section: Section):
        self.sections[section.snum] = section
        pass

    def get_all_courses(self) -> [Course]:
        return self.courses.values()
        pass

    def get_all_courses_by_dept(self, dept) -> [Course]:
        pass

    def get_course(self, dept, cnum) -> Course:
        pass

    def get_all_users(self) -> [User]:
        return self.users.values()
        pass

    def get_user(self, username) -> User:
        pass

    def get_all_sections(self) -> [Section]:
        return self.sections.values()
        pass

    def get_section(self, dept, cnum, snum) -> [Section]:
        pass
