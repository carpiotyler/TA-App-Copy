import unittest
from courseManager import CourseManager
from sectionManager import mySectionManager
from user_manager import UserManager

class sectionTest(unittest.TestCase):

    def setup(self):
        self.course = CourseManager()
        self.course.add(dept="CS", cnum="251")
        self.user = UserManager()
        self.user.add("Bob", "Instructor")
        self.user.add("Rob", "supervisor")
        self.user.add("Randall Cobb", "Instructor")
        self.course.add(dept="CS", cnum="351", ta="Bob", secton="401")
        self.course.add(dept="CS", cnum="251")
        self.sec = mySectionManager()

    def test_add(self):
        self.assertEquals(self.sec.add("CS", "251", "401"), "Section Added: CS-251-401")
        self.assertEquals(self.sec.add("CS", "251", "401", "Bob"), "Section Added: CS-251-401 instructor=Bob")

    def test_addNoInfo(self):
        self.assertRaisesRegex(ValueError, "Could not complete addition, section is needed",
                               self.sec.add(dept="CS", cnum="251"))
        self.assertRaisesRegex(ValueError, "Could not complete addition, section is needed",
                               self.sec.add(dept="CS", cnum="251", ins="Bob"))
        self.assertRaisesRegex(ValueError, "Could not complete addition, course is needed",
                               self.sec.add(dept="CS", snum="401", ins="Bob"))
        self.assertRaisesRegex(ValueError, "Could not complete addition, department is needed",
                               self.sec.add(cnum="251", snum="401", ins="Bob"))

    # user does not exist and shouldn't be able to be added
    def user_none(self):
        self.assertRaisesRegex(RuntimeError, "Nobody does not exist in the system ", self.sec.add(dept="CS", cnum="251", snum="401", ins="Nobody"))

    def test_notQualified(self):
        self.assertRaisesRegex(ValueError, "User can't instruct the course", self.sec.add(dept="CS", cnum="251", snum="401", ins="Rob"))

    def test_alreadyExists(self):
        self.sec.add("CS", "251", "401")
        self.assertRaisesRegex(RuntimeError, "Section already exists", self.sec.add("CS", "251", "401"))

    # test "section view secNum" command output
    def test_view(self):
        self.assertEquals(self.sec.view("CS", "351", "401"), "Course: CS-351\nSection: 401\nInstructor: Bob")

    def test_viewNoInfo(self):
        self.assertRaisesRegex(ValueError, "Could not complete view, section is needed",
                               self.sec.view(dept="CS", cnum="251"))
        self.assertRaisesRegex(ValueError, "Could not complete view, section is needed",
                               self.sec.view(dept="CS", cnum="251", ins="Bob"))
        self.assertRaisesRegex(ValueError, "Could not complete view, course is needed",
                               self.sec.view(dept="CS", snum="401", ins="Bob"))
        self.assertRaisesRegex(ValueError, "Could not complete view, department is needed",
                               self.sec.view(cnum="251", snum="401", ins="Bob"))