import unittest
from Managers.courseManager import CourseManager
from Managers import JSONStorageManager as jsm
import os,json
class CourseTest(unittest.TestCase):

    def setUp(self):
        # In case before testing a tes.json somehow exists
        try:
            self.file = open("coursetest.json", "w")
        except FileNotFoundError:
            pass
        self.file.close()
        os.remove("coursetest.json")
        cm = CourseManager("coursetest.json")
        self.file = None

        self.c.add(dept='CS',cnum='351',instr='Joe')
        self.c.add(dept='CS',cnum='341',instr='Alice')

    def tearDown(self):
        # To remove file (in case of crashes and such during runs before tests do it
        try:
            self.file = open("coursetest.json", "w")
        except FileNotFoundError:
            pass
        self.file.close()
        os.remove("coursetest.json")

    def test_course_add(self):


        self.assertEqual(True,self.cm.add(dept='CS',cnum='359'),"Added Successfully")
        self.assertEqual(True,self.cm.add(dept='CS',cnum='359',instr='Rock',section='901'),"Added Successfully")

    def test_course_add_fail(self):

        self.assertEquals(False,self.cm.add(dept=None, cnum=None))
        self.assertEqual(False,self.cm.add(cnum='351'),"Dept not specified")
        self.assertEqual(False,self.cm.add(cnum='351'),"Dept not specified")
        self.assertEqual(False,self.cm.add(dept='CS'),"Cnum not specified")
        self.assertEqual(False,self.cm.add(dept='CS',cnum='359',instr='Jason'),"Cannot add Intructor with no section")


    def test_course_view(self):

        self.assertEquals("Department: CS\nCourse Number: 351\nSections: []\nCourse Name:\nDescription:\n",self.cm.view(dept='CS',cnum='351'))
        self.assertEquals("CS-331, Instructor: Yang",self.cm.view(dept='CS',cnum='331'))
        self.assertEquals("CS-351, Instructor: Joe \nCS-341, Instructor: Alice \nCS-331, Instructor: Yang",self.cm.view(dept='CS'))

    def test_course_view_no_course(self):

        self.assertEqual("Missing field: dept",self.cm.view(cnum='352'),"Dept is not specified")

        self.assertEquals("Could not be found",self.cm.view(dept='CS',cnum='352'))

    def test_course_view_all(self):
  
        self.assertEquals("CS-351, Instructor: Joe \nCS-341, Instructor: Alice \nCS-331, Instructor: Yang",self.cm.view())

