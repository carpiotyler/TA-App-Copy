import unittest
from courseManager import CourseManager
from sectionManager import sectionManager

class sectionTest(unittest.TestCase):

    def setup(self):
        course = CourseManager()
        course.add("CS", "251")
        set = sectionManager()
    def test_add(self):

        self.assertEquals(set.add("CS", "251", "401"), "Section 401 added to CS-251")

    def test_alreadyExists(self):
        set.add("CS", "251", "401")
        set = sectionManager("CS", "251", "401")
        self.assertEquals(set.add(), "Section 401 already exists in CS-251")

    def test_infoMiss(self):
        set
    # test if calling to add a section that's time conflicts with its lecture fails
    def test_timeConflict(self):
        pass

    # make sure you can't remove a lecture section that has discussions and lab sections attached
    def test_removeLecture(self):
        pass

    # test to make sure adding a section without a lecture can't be done
    def test_discDependency(self):
        pass

    # test that adding a new section with a TA/instructor does not create a conflict in the TA/instructors schedule
    def test_scheduleConflict(self):
        pass

    # make sure "section delete 801" can only delete a disc/lab section and doesn't delete anything else
    def test_delete(self):
        pass

    # test "section view secNum" command output
    def test_view(self):
        pass

