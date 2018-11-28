from Managers.courseManager import CourseManager
<<<<<<< HEAD
from Managers.DjangoStorageManager import DjangoStorageManager
from django.test import TestCase
=======
from TAServer.models import Course, Section, Staff as User
import unittest
import os,json
>>>>>>> 78dd528d98d4d584782f2b9017400a52dc797fbe




class CourseTests(TestCase):

    def setUp(self):
        self.dsm = DjangoStorageManager()
        self.cm = CourseManager(self.dsm)
        self.bad_course1 = {"dept":None, "cnum":None}
        self.bad_course2 = {"dept":'CS'}
        self.bad_course3 = {"cnum":'351'}
        self.bad_course4 = {"dept":'CS', "cnum":'359', "instructor":'Jason'}

        self.good_course1 = {"dept":'CS', "cnum":'351'}
        self.good_course2 = {"dept":'CS', "cnum":'351', "instructor":'Rock', "snum":'901'}
      

    def tearDown(self):
        pass

    def test_course_add(self):

        self.assertEqual(True, self.cm.add(self.good_course1))
        self.assertEqual(True, self.cm.add(self.good_course2))

    def test_course_add_fail(self):

        self.assertEquals(False,self.cm.add(self.bad_course1))
        self.assertEqual(False,self.cm.add(self.bad_course2),"Cnum not specified")
        self.assertEqual(False,self.cm.add(self.bad_course3),"Dept not specified")
        self.assertEqual(False,self.cm.add(self.bad_course4),"Cannot add Intructor with no section")


    def test_course_view(self):

        self.assertEquals("Department: CS\nCourse Number: 351\nSections: []\nCourse Name:\nDescription:\n",self.cm.view(dept='CS',cnum='351'))
        self.assertEquals("Department: CS\nCourse Number: 331\nSections: []\nCourse Name:\nDescription:\n",self.cm.view(dept='CS',cnum='331'))
        self.assertEquals("Department: CS\nCourse Number: 351\nSections: []\nCourse Name:\nDescription:\n\nDepartment: CS\nCourse Number: 341\nSections: []\nCourse Name:\nDescription:\n",self.cm.view(dept='CS'))

    def test_course_view_no_course(self):

        self.assertEqual("Missing field: dept",self.cm.view(cnum='352'),"Dept is not specified")

        self.assertEquals("Could not be found",self.cm.view(dept='CS',cnum='352'))

    def test_course_view_all(self):
  
        self.assertEquals("Department: CS\nCourse Number: 351\nSections: []\nCourse Name:\nDescription:\n\nDepartment: CS\nCourse Number: 341\nSections: []\nCourse Name:\nDescription:\n",self.cm.view(dept='CS'))
