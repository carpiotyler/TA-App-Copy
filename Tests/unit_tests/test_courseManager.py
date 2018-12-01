from Managers.courseManager import CourseManager
from TAServer.models import Section, Course, Staff as User
from Managers.DjangoStorageManager import DjangoStorageManager
from django.test import TestCase



class CourseTests(TestCase):

    def setUp(self):
        self.dsm = DjangoStorageManager
        self.cm = CourseManager(self.dsm)
        self.bad_c1 = {"dept":None, "cnum":None}
        self.bad_c2 = {"dept":'CS'}
        self.bad_c3 = {"cnum":'351'}
        self.bad_c4 = {"dept":'CS', "cnum":'359', "instructor":'Jason'}
        self.bad_c5 = {"dept":'MATH', "cnum":'111'}
        self.bad_c6 = {"dept":'CS', "cnum": 'abc'}

        self.good_c1 = {"dept":'CS', "cnum":'351'}
        self.good_c2 = {"dept":'CS', "cnum":'352', "snum":'901'}
        self.good_c3 = {"dept":'CS', "cnum":'353', "instructor":'Rock', "snum":'902'}
        self.good_c4 = {"dept": 'CS', "cnum": '353', "instructor": 'Yang', "snum": '903', "name": 'Algorithms'}
        self.good_c5 = {"dept": 'CS', "cnum": '354', "instructor": 'Boyland', "snum": '904', "name": 'Discrete', "descr": 'Theory'}


    def tearDown(self):
        pass

    def test_course_add(self):

        self.assertEqual(True, self.cm.add(self.good_c1))
        self.assertEqual(True, self.cm.add(self.good_c2))
        self.assertEqual(True, self.cm.add(self.good_c3))
        self.assertEqual(True, self.cm.add(self.good_c4))
        self.assertEqual(True, self.cm.add(self.good_c5))

    def test_course_add_fail(self):

        self.assertEqual(False, self.cm.add(self.bad_c1), "Dept and Cnum not specified")
        self.assertEqual(False, self.cm.add(self.bad_c2), "Cnum not specified")
        self.assertEqual(False, self.cm.add(self.bad_c3), "Dept not specified")
        self.assertEqual(False, self.cm.add(self.bad_c4), "Cannot add Intructor with no section")
        self.assertEqual(False, self.cm.add(self.bad_c5), "Department not in list of departments")
        self.assertEqual(False, self.cm.add(self.bad_c6), "Cnum must be a number")

    def test_course_view(self):

        self.cm.add(self.good_c1)
        self.cm.add(self.good_c4)
        self.assertEquals("Department: CS Course Number: 351",self.cm.view(self.good_c1))
        self.assertEquals("Department: CS Course Number: 331 Name: Algorithms Instructor: Yang Section: 903",self.cm.view(self.good_c4))

    def test_course_view_no_course(self):

        self.assertEqual("",self.cm.view(self.bad_c3),"Dept is not specified")

        self.assertEquals("Could not be found",self.cm.view(self.good_c1))


    def test_delete(self):
        self.cm.add(self.good_c1)
        self.cm.add(self.good_c2)

        self.assertEqual(False, self.cm.add(self.bad_c1), "Dept and Cnum not specified")
        self.assertEqual(False, self.cm.add(self.bad_c2), "Cnum not specified")
        self.assertEqual(False, self.cm.add(self.bad_c3), "Dept not specified")

        self.assertEqual(True, self.cm.delete(self.good_c2), "Success")
        self.assertEqual(False, self.cm.delete(self.good_c4), "Course Not Found")



