import unittest
from Managers.courseManager import CourseManager

class CourseTest(unittest.TestCase):
    def setUp(self):
        self.c = CourseManager()

        self.c.add(dept='CS',cnum='351',instr='Joe')
        self.c.add(dept='CS',cnum='341',instr='Alice')
        self.c.add(dept='CS',cnum='331',instr='Yang')

    def tearDown(self):
        pass

    def test_course_add(self):

        self.assertEqual(False,self.c.add(dept='CS',cnum='359',instr='Jason'),"Cannot add Intructor with no section")
        self.assertEqual(True,self.c.add(dept='CS',cnum='359'),"Added Successfully")

    def test_course_add_fail(self):

        self.assertEquals("Cnum not specified, course not added.",self.c.add(dept='CS'))
        self.assertEquals("Dept not specified, course not added.",self.c.add(cnum='351'))

    def test_course_view(self):

        self.assertEquals("CS-351, Instructor: Joe",self.c.view(dept='CS',cnum='351'))
        self.assertEquals("CS-331, Instructor: Yang",self.c.view(dept='CS',cnum='331'))
        self.assertEquals("CS-351, Instructor: Joe \nCS-341, Instructor: Alice \nCS-331, Instructor: Yang",self.c.view(dept='CS'))

    def test_course_view_no_course(self):

        self.assertEquals("No course available",self.c.view(cnum='352'))
        self.assertEquals("No course available",self.c.view(dept='CS',cnum='352'))

    def test_course_view_all(self):
  
        self.assertEquals("CS-351, Instructor: Joe \nCS-341, Instructor: Alice \nCS-331, Instructor: Yang",self.c.view())

    def test_course_edit(self):
        
        self.assertEquals("Edit Successful",self.c.edit(dept='CS',cnum='351',instr='None'))

        self.assertEquals("CS-351, Instructor: None \nCS-341, Instructor: Alice \nCS-331, Instructor: Yang",self.c.view())

    def test_course_edit_unsuccessful(self):
        
        self.assertEquals("Edit Unsuccessful, course not found",self.c.edit(dept='CS',cnum='361',instr='None'))
        self.assertEquals("CS-351, Instructor: Joe \nCS-341, Instructor: Alice \nCS-331, Instructor: Yang",self.c.view())

    def test_course_delete(self):

        self.c.delete(dept='CS',cnum='341')

        self.assertEquals("CS-351, Instructor: Joe \nCS-331, Instructor: Yang",self.c.view())

    def test_course_delete_unsuccessful(self):

        self.c.delete(dept='CS',cnum='311')

        self.assertEquals("CS-351, Instructor: Joe \nCS-341, Instructor: Alice \nCS-331, Instructor: Yang",self.c.view())

