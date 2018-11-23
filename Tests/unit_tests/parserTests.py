import unittest
from CmdParser import CommandParser as parser
from Managers.userManager import UserManager
from Managers.sectionManager import mySectionManager
from Managers.courseManager import CourseManager
from Managers.ManagerInterface import ManagerInterface
from Managers.myStorageManager import AbstractStorageManager
from Managers.JSONStorageManager import JSONStorageManager
from Managers.authManager import AuthManager
from Domain.user import User # Eventually change this to models


# This is the base class for all the testing versions of their respective classes. The main difference is in order to
# not bread the parser at runtime and maintain return types a new function has been added called getDict which returns
# the last dict passed as an argument to any of the functions. Im my eyes this is a better solution to having to return
# weird strings in the parser and having to tell the parser if its being unittested or not. Any function that normally
# returns a boolean returns False and all functions that return a string just return an empty string. (Hopefully this
# doesn't fuck everything up).
class TM(ManagerInterface):
    def __init__(self, database: AbstractStorageManager=JSONStorageManager()):
        super().__init__(database)  # This is just so pycharm will stop being mad at me
        self.lastDict = {}  # To hold the last dict given to the class

    def add(self, fields: dict)->bool:
        fields['command'] = 'add'
        self.lastDict = fields
        return False

    def view(self, fields: dict)->str:
        fields['command'] = 'view'
        self.lastDict = fields
        return ""

    def edit(self, fields: dict)->bool:
        fields['command'] = 'edit'
        self.lastDict = fields
        return False

    def delete(self, fields: dict)->bool:
        fields['command'] = 'delete'
        self.lastDict = fields
        return False

    def getDict(self)->dict:
        return self.lastDict


# This is the version of CourseManager to be used for testing. The big four commands (add, view, edit, and delete) are
# all inherited from TM (because it is first in the inheritance) and reqFields and optFields come from CourseManager
# giving this testing class the best of both worlds. The code I had before (to make sure the functions I wanted) were
# being called is still there, just commented out, in the case that this doesn't work how I think it'll work. This is
# how the TCM, TSM, and TUM work.
class TCM(TM, CourseManager):
    def __init__(self, database: AbstractStorageManager=JSONStorageManager()):
        TM.__init__(self, database)
        CourseManager.__init__(self, database)

    # def add(self, fields: dict)->bool:
    #     return TM.add(self, fields)
    #
    # def view(self, fields: dict)->str:
    #     return TM.view(self, fields)
    #
    # def edit(self, fields: dict)->bool:
    #     return TM.edit(self, fields)
    #
    # def delete(self, fields: dict)->bool:
    #     return TM.delete(self, fields)
    #
    # @staticmethod
    # def reqFields()->list:
    #     return CourseManager.reqFields()
    #
    # @staticmethod
    # def optFields()->list:
    #     return CourseManager.optFields()


# Check TCM
class TSM(TM, mySectionManager):
    def __init__(self, database: AbstractStorageManager=JSONStorageManager()):
        TM.__init__(self, database)
        mySectionManager.__init__(self, database)

    # def add(self, fields: dict)->bool:
    #     return TM.add(self, fields)
    #
    # def view(self, fields: dict)->str:
    #     return TM.view(self, fields)
    #
    # def edit(self, fields: dict)->bool:
    #     return TM.edit(self, fields)
    #
    # def delete(self, fields: dict)->bool:
    #     return TM.delete(self, fields)
    #
    # @staticmethod
    # def reqFields()->list:
    #     return mySectionManager.reqFields()
    #
    # @staticmethod
    # def optFields()->list:
    #     return mySectionManager.optFields()


# Check TCM
class TUM(TM, UserManager):
    def __init__(self, database: AbstractStorageManager=JSONStorageManager()):
        TM.__init__(self, database)
        UserManager.__init__(self, database)

    # def add(self, fields: dict)->bool:
    #     return TM.add(self, fields)
    #
    # def view(self, fields: dict)->str:
    #     return TM.view(self, fields)
    #
    # def edit(self, fields: dict)->bool:
    #     return TM.edit(self, fields)
    #
    # def delete(self, fields: dict)->bool:
    #     return TM.delete(self, fields)
    #
    # @staticmethod
    # def reqFields()->list:
    #     return UserManager.reqFields()
    #
    # @staticmethod
    # def optFields()->list:
    #     return UserManager.optFields()


# This test version is a little different from the rest because AuthManager does not implement the manager interface.
# This has all the same functions as AuthManager except they either return an empty string or True when appropriate.
# Except for login which returns the current user that can be set by the function setUser.
class TAM(AuthManager):
    def __init__(self, usermgr: UserManager):
        AuthManager.__init__(usermgr)
        self.user = None

    def setUser(self, u: User):
        self.user = u

    def login(self, username: str, password: str)->User:
        return self.user

    def logout(self, u: User)->str:
        return ""

    def validate(self, command: str)->bool:
        return True


# This is all the test cases. Only the big three commands are tested (course, section, and user). This only tests that
# the right helper function is called and the right params are given to the manager.
class ParserTest(unittest.TestCase):
    def setUp(self):
        self.usermgr = TUM()
        self.sectmgr = TSM()
        self.coursemgr = TCM()
        self.authmgr = TAM(self.usermgr)
        self.p = parser(self.sectmgr, self.usermgr, self.coursemgr, self.authmgr)

    def tearDown(self):
        pass

    def test_courseAdd(self):
        self.p.parse("course add code=CS-351-601")
        self.assertDictEqual(self.coursemgr.getDict(), {'dnum': 'CS', 'cnum': '351', 'snum': '601', 'command': 'add'})

    def test_courseEditByCode(self):
        self.p.parse("course edit code=CS-550 ins=Danny")
        self.assertDictEqual(self.coursemgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'command': 'add', 'ins': 'Danny'})

    def test_courseEditByNums(self):
        self.p.parse("course edit dept=CS cnum=550 ins=Danny")
        self.assertDictEqual(self.coursemgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'command': 'add', 'ins': 'Danny'})

    def test_courseViewAll(self):
        self.p.parse("course view")
        self.assertDictEqual(self.coursemgr.getDict(), {'command': 'view'})

    def test_courseViewOneByCode(self):
        self.p.parse("course view code=CS-550")
        self.assertDictEqual(self.coursemgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'command': 'view'})

    def test_courseViewOneByNums(self):
        self.p.parse("course view dept=CS cnum=550")
        self.assertDictEqual(self.coursemgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'command': 'view'})

    def test_courseDeleteByCode(self):
        self.p.parse("course delete code=CS-550")
        self.assertDictEqual(self.coursemgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'command': 'delete'})

    def test_courseDeleteByNums(self):
        self.p.parse("course delete dept=CS cnum=550")
        self.assertDictEqual(self.coursemgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'command': 'delete'})

    def test_sectionAdd(self):
        self.p.parse("section add dept=CS cnum=550 snum=601")
        self.assertDictEqual(self.sectmgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'snum': '601', 'command': 'add'})

    def test_sectionEditByCode(self):
        self.p.parse("section edit code=CS-550-601 ins=Danny")
        self.assertDictEqual(self.sectmgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'snum': '601', 'ins': 'Danny', 'command': 'edit'})

    def test_sectionEditByNums(self):
        self.p.parse("section edit dept=CS cnum=550 snum=601 ins=Danny")
        self.assertDictEqual(self.sectmgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'snum': '601', 'ins': 'Danny', 'command': 'edit'})

    def test_sectionViewOneByCode(self):
        self.p.parse("section view code=CS-351-601")
        self.assertDictEqual(self.sectmgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'snum': '601', 'command': 'view'})

    def test_sectionViewOneByNums(self):
        self.p.parse("section view dept=CS cnum=550 snum=601")
        self.assertDictEqual(self.sectmgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'snum': '601', 'command': 'view'})

    def test_sectionViewAll(self):
        self.p.parse("section view")
        self.assertDictEqual(self.sectmgr.getDict(), {'command': 'view'})

    def test_sectionDeleteByCode(self):
        self.p.parse("section delete code=CS-550-601")
        self.assertDictEqual(self.sectmgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'snum': '601', 'command': 'delete'})

    def test_sectionDeleteByNums(self):
        self.p.parse("section delete dept=CS cnum=550 snum=601")
        self.assertDictEqual(self.sectmgr.getDict(), {'dnum': 'CS', 'cnum': '550', 'snum': '601', 'command': 'delete'})

    def test_userAdd(self):
        self.p.parse("user add user=Danny pass=1234")
        self.assertDictEqual(self.usermgr.getDict(), {'command': 'add', 'user': 'Danny', 'pass': '1234'})

    def test_userEdit(self):
        self.p.parse("user edit user=Danny role=TA")
        self.assertDictEqual(self.usermgr.getDict(), {'command': 'edit', 'user': 'Danny', 'role': 'TA'})

    def test_userViewOne(self):
        self.p.parse("user view user=Danny")
        self.assertDictEqual(self.usermgr.getDict(), {'command': 'view', 'user': 'Danny'})

    def test_userViewAll(self):
        self.p.parse("user view")
        self.assertDictEqual(self.usermgr.getDict(), {'command': 'view'})

    def test_userDelete(self):
        self.p.parse("user delete user=Danny")
        self.assertDictEqual(self.usermgr.getDict(), {'command': 'delete', 'user': 'Danny'})


if __name__ == '__main__':  # Just a placeholder until a real test runner is written
    unittest.main()
