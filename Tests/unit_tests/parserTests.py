import unittest
from CmdParser import CommandParser as parse

# This class contains the unit tests for the command parser check CmdParser.py for better descriptions of how the
# functions work. A useful thing to note is that the parse function has 3 fields, the command string, the optional user
# object, and the option testing boolean. If testing is True, then the user does not matter. The parse function is the
# only one tested by this class because the rest of the helper functions should be treated as private.


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.p = parse(True)

    def tearDown(self):
        pass

    def test_courseAdd(self):
        self.assertEqual('%s.add(dept="CS", cnum="550", section="None", ins="None")' % self.p.namesdict['course'],
                         self.p.parse("course add dept=CS cnum=550"))

    def test_courseEditByCode(self):
        self.assertEqual('%s.edit(dept="CS", cnum="550", section="None", ins="Danny")' % self.p.namesdict['course'],
                         self.p.parse("course edit code=CS-550 ins=Danny"))

    def test_courseEditByNums(self):
        self.assertEqual('%s.edit(dept="CS", cnum="550", section="None", ins="Danny")' % self.p.namesdict['course'],
                         self.p.parse("course edit dept=CS cnum=550 ins=Danny"))

    def test_courseViewAll(self):
        self.assertEqual('%s.view()' % self.p.namesdict['course'],
                         self.p.parse("course view"))

    def test_courseViewOneByCode(self):
        self.assertEqual(('%s.view(dept="CS", cnum="351", section="None", ins="None")' % self.p.namesdict['course']),
                         self.p.parse("course view code=CS-351"))

    def test_courseViewOneByNums(self):
        self.assertEqual(('%s.view(dept="CS", cnum="351", section="None", ins="None")' % self.p.namesdict['course']),
                         self.p.parse("course view dept=CS cnum=351"))

    def test_courseDeleteByCode(self):
        self.assertEqual('%s.delete(dept="CS", cnum="351", section="None", ins="None")' % self.p.namesdict['course'],
                         self.p.parse("course delete code=CS-351"))

    def test_courseDeleteByNums(self):
        self.assertEqual('%s.delete(dept="CS", cnum="351", section="None", ins="None")' % self.p.namesdict['course'],
                         self.p.parse("course delete code=CS-351"))

    def test_sectionAdd(self):
        self.assertEqual('%s.add(dept="CS", cnum="550", snum="601", ins="None")' % self.p.namesdict['section'],
                         self.p.parse("section add dept=CS cnum=550 snum=601"))

    def test_sectionEditByCode(self):
        self.assertEqual('%s.edit(dept="CS", cnum="550", snum="601", ins="Danny")' % self.p.namesdict['section'],
                         self.p.parse("section edit code=CS-550-601 ins=Danny"))

    def test_sectionEditByNums(self):
        self.assertEqual('%s.edit(dept="CS", cnum="550", snum="601", ins="Danny")' % self.p.namesdict['section'],
                         self.p.parse("section edit dept=CS cnum=550 snum=601 ins=Danny"))

    def test_sectionViewOneByCode(self):
        self.assertEqual(('%s.view(dept="CS", cnum="351", snum="601", ins="None")' % self.p.namesdict['section']),
                         self.p.parse("section view code=CS-351-601"))

    def test_sectionViewOneByNums(self):
        self.assertEqual(('%s.view(dept="CS", cnum="550", snum="601", ins="None")' % self.p.namesdict['section']),
                         self.p.parse("section view dept=CS cnum=550 snum=601"))

    def test_sectionViewAll(self):
        self.assertEqual('%s.view()' % self.p.namesdict['section'],
                         self.p.parse("section view"))

    def test_sectionDeleteByCode(self):
        self.assertEqual('%s.delete(dept="CS", cnum="351", snum="601", ins="None")' % self.p.namesdict['section'],
                         self.p.parse("section delete code=CS-351-601"))

    def test_sectionDeleteByNums(self):
        self.assertEqual('%s.delete(dept="CS", cnum="550", snum="601", ins="None")' % self.p.namesdict['section'],
                         self.p.parse("section delete dept=CS cnum=550 snum=601"))

    def test_userAdd(self):
        self.assertEqual('%s.add("Danny", password="1234", role="None")' % self.p.namesdict['user'],
                         self.p.parse("user add user=Danny pass=1234"))

    def test_userEdit(self):
        self.assertEqual('%s.edit("Danny", password="None", role="TA")' % self.p.namesdict['user'],
                         self.p.parse("user edit user=Danny role=TA"))

    def test_userViewOne(self):
        self.assertEqual('%s.view("Danny")' % self.p.namesdict['user'],
                         self.p.parse("user view user=Danny"))

    def test_userViewAll(self):
        self.assertEqual('%s.view()' % self.p.namesdict['user'],
                         self.p.parse("user view"))

    def test_userDelete(self):
        self.assertEqual('%s.delete("Danny")' % self.p.namesdict['user'],
                         self.p.parse("user delete user=Danny"))


if __name__ == '__main__':  # Just a placeholder until a real test runner is written
    unittest.main()