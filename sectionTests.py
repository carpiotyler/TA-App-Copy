import unittest
from courseManager import CourseManager
from sectionManager import sectionManager
from userManager import UserManager

class sectionTest(unittest.TestCase):

    def setup(self):
        self.course = CourseManager()
        self.course.add(dept="CS", cnum="251")
        self.user.add("Bob")
        self.user.add("Rob")
        self.sec = sectionManager()

    def test_add(self):
        self.assertEquals(self.sec.add("CS", "251", "401"), "Section 401 added to CS-251")

    def test_alreadyExists(self):
        self.sec.add("CS", "251", "401")
        self.assertEquals(self.sec.add("CS", "251", "401"), "Section 401 already exists in CS-251")

    # test if calling to add a section that's time conflicts with its lecture fails
    def test_timeConflict(self):
        pass

    # test to make sure adding a section without a lecture can't be done
    def test_discDependency(self):
        self.assertEquals(self.sec.add("CS", "251", "801"), "CS-251 needs a lecture section before adding "
                                                            "disc/lab section")

    # test that adding a new section with a TA/instructor does not create a conflict in the TA/instructors schedule
    def test_scheduleConflict(self):
        pass

    # make sure "section delete 801" can only delete a disc/lab section and doesn't delete anything else
    def test_delete(self):
        self.sec.add("CS", "251", "401")
        self.sec.add("CS", "251", "801")
        self.assertEquals(self.sec.delete("CS", "251", "401"), "Delete failed. Lecture could not be deleted "
                                                               "because a discussion/lab depends on it")

    # test "section view secNum" command output
    def test_view(self):
        pass

    def test_edit(self):
        self.sec.add("CS", "251", "401", "Rob")
        self.assertEquals(self.sec.edit("CS", "251", "401", "Bob"), "Successfully changed TA to Bob")
        self.assertEquals(self.edit("CS", "251", "402", "Rob"), "Section does not exist")

