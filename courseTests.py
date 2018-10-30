import unittest
from courseManager import CourseManager

class CourseTest(unittest.TestCase):
    def setUp(self):
        self.c = CourseManager()

    def tearDown(self):
        pass

    def test_course_add(self):
        self.assertEquals("Successfully Added Course",self.c.add(dept='CS',cnum='351',ta='Joe'))
        self.assertEquals("Successfully Added Course",self.c.add(dept='CS',cnum='351'))

    def test_course_add_fail(self):
        self.assertEquals("Cnum not specified, course not added.",self.c.add(dept='CS'))
        self.assertEquals("Dept not specified, course not added.",self.c.add(cnum='351'))

    def test_course_view(self):
        self.c.add(dept='CS',cnum='351',ta='Joe')
        self.c.add(dept='CS',cnum='341',ta='Alice')
        self.c.add(dept='CS',cnum='331',ta='Yang')

        self.assertEquals("CS-351, TA: Joe",self.c.view(dept='CS',cnum='351'))
        self.assertEquals("CS-331, TA: Yang",self.c.view(dept='CS',cnum='331'))
        self.assertEquals("CS-351, TA: Joe \nCS-341, TA: Alice \nCS-331, TA: Yang",self.c.view(dept='CS'))

    def test_course_view_no_course(self):
        self.c.add(dept='CS',cnum='351',ta='Joe')
        self.assertEquals("No course available",self.c.view(cnum='352'))
        self.assertEquals("No course available",self.c.view(dept='CS',cnum='352'))

    def test_course_view_all(self):
        self.c.add(dept='CS',cnum='351',ta='Joe')
        self.c.add(dept='CS',cnum='341',ta='Alice')
        self.c.add(dept='CS',cnum='331',ta='Yang')

        self.assertEquals("CS-351, TA: Joe \nCS-341, TA: Alice \nCS-331, TA: Yang",self.c.view())

    def test_course_edit(self):
        self.c.add(dept='CS',cnum='351',ta='Joe')
        
        self.assertEquals("Edit Successful",self.c.edit(dept='CS',cnum='351',ta='None'))

        self.assertEquals("CS-351, TA: None",self.c.view())

    def test_course_edit_unsuccessful(self):
        self.c.add(dept='CS',cnum='351',ta='Joe')
        
        self.assertEquals("Edit Unsuccessful, course not found",self.c.edit(dept='CS',cnum='361',ta='None'))
        self.assertEquals("CS-351, TA: Joe",self.c.view())

    def test_course_delete(self):
        self.c.add(dept='CS',cnum='351',ta='Joe')
        self.c.add(dept='CS',cnum='341',ta='Alice')
        self.c.add(dept='CS',cnum='331',ta='Yang')

        self.c.delete(dept='CS',cnum='341')

        self.assertEquals("CS-351, TA: Joe \nCS-331, TA: Yang",self.c.view())

    def test_course_delete_unsuccessful(self):
        self.c.add(dept='CS',cnum='351',ta='Joe')
        self.c.add(dept='CS',cnum='341',ta='Alice')
        self.c.add(dept='CS',cnum='331',ta='Yang')

        self.c.delete(dept='CS',cnum='311')

        self.assertEquals("CS-351, TA: Joe \nCS-341, TA: Alice \nCS-331, TA: Yang",self.c.view())

