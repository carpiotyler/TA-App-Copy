import unittest
from courseManager import CourseManager
from sectionManager import mySectionManager
from user_Manager import UserManager

class sectionTest(unittest.TestCase):

    def setup(self):
        self.course = CourseManager()
        self.course.add(dept="CS", cnum="251")
        self.user.add("Bob", "Instructor")
        self.user.add("Rob", "TA")
        self.user.add("Randall Cobb", "Instructor")
        self.course.add(dept="CS", cnum="351", ta="Bob", secton="401")
        self.sec = mySectionManager()

    def test_add(self):
        self.assertEquals(self.sec.add("CS", "251", "401"), "Section Added: CS-251-401")
        self.assertEquals(self.sec.add("CS", "251", "401", "Bob"), "Section Added: CS-251-401 instructor= Bob")

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
        self.assertEquals(self.sec.add(dept="CS", cnum="251", snum="401", ins="Rob"), "Rob can't teach lectures")

    def test_alreadyExists(self):
        self.sec.add("CS", "251", "401")
        self.assertRaisesRegex(RuntimeError, "Section already exists", self.sec.add("CS", "251", "401"))

    # test if calling to add a section that's time conflicts with its lecture fails
    """No time has been implemented yet"""
    def test_timeConflict(self):
        pass

    # make sure "section delete 801" can only delete a disc/lab section and doesn't delete anything else
    def test_delete(self):
        self.sec.add("CS", "251", "401")
        self.sec.add("CS", "251", "801")
        self.assertEquals(self.sec.delete("CS", "251", "401"), "Delete failed. Lecture could not be deleted "
                                                               "because a discussion/lab depends on it")

    # test "section view secNum" command output
    """I don't know if the output is correct"""
    def test_view(self):
        self.assertEquals(self.sec.view("CS", "351", "401"), "Instructor=Bob")

    def test_edit(self):
        self.sec.add("CS", "251", "401", "Rob")
        self.assertEquals(self.sec.edit("CS", "251", "401", "Bob"), "Successfully changed TA to Bob")
        self.assertEquals(self.edit("CS", "251", "402", "Rob"), "Section does not exist")

