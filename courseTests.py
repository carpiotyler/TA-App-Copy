import unittest
from courseManager import CourseManager

class CourseTest(unittest.TestCase):
    def setUp(self):
        c = CourseManager()

    def tearDown(self):
        pass

    def test_courseAdd(self):
        self.assertEquals("Successfully Added Course",c.add(dept='CS',cnum='351',ta='Joe'))
        self.assertEquals("Successfully Added Course",c.add(dept='CS',cnum='351'))

    def test_courseAddFail(self):
        self.assertEquals("Cnum not specified, course not added.",c.add(dept='CS'))
        self.assertEquals("Dept not specified, course not added.",c.add(cnum='351'))

    def test_courseView(self):
        c.add(dept='CS',cnum='351',ta='Joe')
        c.add(dept='CS',cnum='341',ta='Alice')
        c.add(dept='CS',cnum='331',ta='Yang')
        
        self.assertEquals("CS-351, TA: Joe",c.view(dept='CS',cnum='351'))
        self.assertEquals("CS-331, TA: Yang",c.view(dept='CS',cnum='331'))
        self.assertEquals("CS-351, TA: Joe \nCS-341, TA: Alice \nCS-331, TA: Yang",c.view(dept='CS'))

    def test_courseViewAll(self):
        c.add(dept='CS',cnum='351',ta='Joe')
        c.add(dept='CS',cnum='341',ta='Alice')
        c.add(dept='CS',cnum='331',ta='Yang')

        self.assertEquals("CS-351, TA: Joe \nCS-341, TA: Alice \nCS-331, TA: Yang",c.view())
