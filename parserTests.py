import unittest
from parser import CommandParser as cp

# This class contains the unit tests for the command parser check parser.py for better descriptions of how the functions
# work. A useful thing to note is that the parse function has 3 fields, the command string, the optional user object,
# and the option testing boolean. If testing is True, then the user does not matter. The parse function is the only one
# tested by this class because the rest of the helper functions should be treated as private.


class ParserTest(unittest.TestCase):
    def setup(self):
        cp.uting = True

    def tearDown(self):
        cp.uting = False

    def test_courseAdd(self):
        pass

    def test_courseEdit(self):
        pass

    def test_courseView(self):
        pass

    def test_courseDelete(self):
        pass

    def test_sectionAdd(self):
        pass

    def test_sectionEdit(self):
        pass

    def test_sectionView(self):
        pass

    def test_sectionDelete(self):
        pass

    def test_userAdd(self):
        pass

    def test_userEdit(self):
        pass

    def test_userView(self):
        pass

    def test_userDelete(self):
        pass

    def test_departmentAdd(self):
        pass

    def test_departmentEdit(self):
        pass

    def test_departmentView(self):
        pass

    def test_departmentDelete(self):
        pass


if __name__ == '__main__':  # Just a placeholder until a real test runner is written
    unittest.main()