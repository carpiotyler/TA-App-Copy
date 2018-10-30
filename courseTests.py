import unittest
from courseManager import CourseManager

class CourseTest(unittest.TestCase):
    def setUp(self):
        c = CourseManager()

    def tearDown(self):
        pass

    def test_course_add(self):
        self.assertEquals("Successfully Added Course",c.add(dept='CS',cnum='351',ta='Joe'))
        self.assertEquals("Successfully Added Course",c.add(dept='CS',cnum='351'))

    def test_course_add_fail(self):
        self.assertEquals("Cnum not specified, course not added.",c.add(dept='CS'))
        self.assertEquals("Dept not specified, course not added.",c.add(cnum='351'))

    def test_course_view(self):
        c.add(dept='CS',cnum='351',ta='Joe')
        c.add(dept='CS',cnum='341',ta='Alice')
        c.add(dept='CS',cnum='331',ta='Yang')

        self.assertEquals("CS-351, TA: Joe",c.view(dept='CS',cnum='351'))
        self.assertEquals("CS-331, TA: Yang",c.view(dept='CS',cnum='331'))
        self.assertEquals("CS-351, TA: Joe \nCS-341, TA: Alice \nCS-331, TA: Yang",c.view(dept='CS'))

    def test_course_view_no_course(self):
        c.add(dept='CS',cnum='351',ta='Joe')
        self.assertEquals("No course available",c.view(cnum='352'))
        self.assertEquals("No course available",c.view(dept='CS',cnum='352'))

    def test_course_view_all(self):
        c.add(dept='CS',cnum='351',ta='Joe')
        c.add(dept='CS',cnum='341',ta='Alice')
        c.add(dept='CS',cnum='331',ta='Yang')

        self.assertEquals("CS-351, TA: Joe \nCS-341, TA: Alice \nCS-331, TA: Yang",c.view())

    def test_course_edit(self):
        c.add(dept='CS',cnum='351',ta='Joe')
        
        self.assertEquals("Edit Successfull",c.edit(dept='CS',cnum='351',ta='None'))
        self.assertEquals("CS-351, TA: Joe",c.view())
        self.assertEquals("CS-351, TA: None",c.view())

    def test_course_edit_unsuccessful(self):
        c.add(dept='CS',cnum='351',ta='Joe')
        
        self.assertEquals("Edit Unsuccessful, course not found",c.edit(dept='CS',cnum='361',ta='None'))
        self.assertEquals("CS-351, TA: Joe",c.view())

 