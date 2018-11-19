import unittest
from TAServer.models import Section, Course, User
from Managers.DjangoSectionManager import SectionManager as SM

class sectionTest(unittest.TestCase):

    def setUp(self):

        self.u1 = User(username="Gumby", first_name="Gimpy", last_name="McGoo",
                 email="Gumby@gmail.com", password="123", role="instructor")
        self.u1.save()
        self.c1 = Course(cnum=351, name="Data Structures and Algorithms",
                    description="N/A", dept="CS")
        self.c1.save()
        self.s1 = Section(snum=401, stype="lecture", course=c1, room=395, instructor=u1,
                     days="MW", time="12:30 PM")
        self.s1.save()
        self.sec = SM()

    def tearDown(self):
        pass

    # Test correct adding
    def test_add(self):
        newSec = {snum : 801, stype: "lab", course: self.c1, room: 901, instructor: self.u1, days: "T", time: "4:00 PM"}
        self.assertTrue(sec.add(newSec), "New section was not added")

    # Test adding without requirements (course, instructor, snum)
    def test_addNoInfo(self):
        secNoCourse= {snum: 401, instructor: self.u1}
        secNoSnum= {course: self.c1, instructor: self.u1}
        secNoIns= {snum: 401, course: self.c1}
        self.assertFalse(self.sec.add(secNoCourse), "Should return false when no course is specified")
        self.assertFalse(self.sec.add(secNoSnum), "Should return false when no section number is specified")
        self.assertFalse(self.sec.add(secNoIns), "Should return false when no instructor is specified")

    # user does not exist and shouldn't be able to be added
    def test_userNone(self):
        u2 = User(username="Bubba", first_name="Bubba", last_name="Gump",
                 email="BubbaGump@gmail.com", password="shrimp", role="TA")
        secUserInv= {snum: 801, instructor: u2, course:self.c1}
        self.assertFalse(self.sec.add(secUserInv), "User Bubba does not exist in the system")

    # user is not a ta or instructor
    def test_notQualified(self):
        u2 = User(username="Bubba", first_name="Bubba", last_name="Gump",
                 email="BubbaGump@gmail.com", password="shrimp", role="administrator")
        secUserInv = {snum: 801, instructor: u2, course: self.c1}
        self.assertFalse(self.sec.add(secUserInv), "User is not qualified to instruct a class")

    # test "section view secNum" command output
    def test_view(self):
        toView= {snum:401, course:self.c1}
        self.assertEqual(self.sec.view(toView),
                         "Course: CS-351\nSection: 401\nInstructor: Bob")

    # Test to make sure a course without a section will not be found
    def test_viewNot(self):
        self.courseT = Course(cnum=337, name="Systems Programming",
                    description="N/A", dept="CS")
        self.courseT.save()
        toView = {snum:401, instructor: self.u1, course:self.courseT}
        self.assertEqual("Could not find CS-337-401", self.sec.view(toView))

    # Test view without enough information
    def test_viewNoInfo(self):
        secNoCourse= {snum: 401, instructor: self.u1}
        secNoSnum= {course: self.c1, instructor: self.u1}
        self.assertEqual(self.sec.view(secNoCourse), "Could not view, no course specified",
                         "Should not be able to view without course specified")
        self.assertEqual(self.sec.view(secNoSnum), "Could not view, no section number specified",
                         "Should not be able to view without section number specified")
