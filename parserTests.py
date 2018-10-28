import unittest
from CmdParser import CommandParser as p

# This class contains the unit tests for the command parser check CmdParser.py for better descriptions of how the
# functions work. A useful thing to note is that the parse function has 3 fields, the command string, the optional user
# object, and the option testing boolean. If testing is True, then the user does not matter. The parse function is the
# only one tested by this class because the rest of the helper functions should be treated as private.


class ParserTest(unittest.TestCase):
    def setUp(self):
        p.uting = True

    def tearDown(self):
        p.uting = False

    def test_courseAdd(self):
        self.assertEqual('%s.add(dept="CS", cnum="550")' % p.namesdict['course'],
                         p.parse("course add dept=CS cnum=550"))

    def test_courseEditByCode(self):
        self.assertEqual('%s.edit(code="CS-550", TA="Danny"' % p.namesdict['course'],
                         p.parse("course edit code=CS-550 TA=Danny"))

    def test_courseEditByNums(self):
        self.assertEqual('%s.edit(dnum="CS", cnum="550", TA="Danny"' % p.namesdict['course'],
                         p.parse("course edit dnum=CS cnum=550 TA=Danny"))

    def test_courseViewAll(self):
        self.assertEqual('%s.view()' % p.namesdict['course'],
                         p.parse("course view"))

    def test_courseViewOneByCode(self):
        self.assertEqual(('%s.view(code="CS-351")' % p.namesdict['course']),
                         p.parse("course view CS-351"))

    def test_courseViewOneByNums(self):
        self.assertEqual(('%s.view(dnum="CS", cnum="351")' % p.namesdict['course']),
                         p.parse("course view dnum=CS cnum=351"))

    def test_courseDeleteByCode(self):
        self.assertEqual('%s.delete(code="CS-351")' % p.namesdict['course'],
                         p.parse("course delete CS-351"))

    def test_courseDeleteByNums(self):
        self.assertEqual('%s.delete(dnum="CS", cnum="351")' % p.namesdict['course'],
                         p.parse("course delete CS-351"))

    def test_sectionAdd(self):
        self.assertEqual('%s.add(dept="CS", cnum="550", snum="601")' % p.namesdict['section'],
                         p.parse("section add dept=CS cnum=550 snum=601"))

    def test_sectionEditByCode(self):
        self.assertEqual('%s.edit(code="CS-550-601", TA="Danny"' % p.namesdict['section'],
                         p.parse("section edit code=CS-550-601 TA=Danny"))

    def test_sectionEditByNums(self):
        self.assertEqual('%s.edit(dnum="CS", cnum="550", snum="601", TA="Danny"' % p.namesdict['section'],
                         p.parse("section edit dnum=CS cnum=550 snum=601 TA=Danny"))

    def test_sectionViewOneByCode(self):
        self.assertEqual(('%s.view(code="CS-351-601")' % p.namesdict['section']),
                         p.parse("section view CS-351"))

    def test_sectionViewOneByNums(self):
        self.assertEqual(('%s.view(dnum="CS", cnum="550", snum="601")' % p.namesdict['section']),
                         p.parse("section view dnum=CS cnum=550 snum=601"))

    def test_sectionViewAll(self):
        self.assertEqual('%s.view()' % p.namesdict['section'],
                         p.parse("section view"))

    def test_sectionDeleteByCode(self):
        self.assertEqual('%s.delete(code="CS-351-601")' % p.namesdict['section'],
                         p.parse("section delete CS-351"))

    def test_sectionDeleteByNums(self):
        self.assertEqual('%s.delete(dnum="CS", cnum="550", snum="601")' % p.namesdict['section'],
                         p.parse("section delete dnum=CS cnum=550 snum=601"))

    def test_userAdd(self):
        self.assertEqual('%s.add(username="Danny", password="1234"' % p.namesdict['user'],
                         p.parse("user add username=Danny password=1234"))

    def test_userEdit(self):
        self.assertEqual('%s.edit(username="Danny", role="TA"' % p.namesdict['user'],
                         p.parse("user edit username=Danny role=TA"))

    def test_userViewOne(self):
        self.assertEqual('%s.view(username="Danny")' % p.namesdict['user'],
                         p.parse("user view username=Danny"))

    def test_userViewAll(self):
        self.assertEqual('%s.view()' % p.namesdict['user'],
                         p.parse("user view"))

    def test_userDelete(self):
        self.assertEqual('%s.delete(username="Danny")' % p.namesdict['user'],
                         p.parse("user delete username=Danny"))

if __name__ == '__main__':  # Just a placeholder until a real test runner is written
    unittest.main()