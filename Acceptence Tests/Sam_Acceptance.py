import unittest
from Skeleton import Project


# Test TA method
class TestTA(unittest.TestCase):

    # Edit contact info #15
    def contactNoLoggin(self):
        mySetup = Project()

        self.assertEqual(mySetup.command("user edit phone (414)883-4893"), "You need to login before you can edit contact information",
                         "Test failed. Should not have been able to edit without logging in")

    def editContactInfo(self):

        mySetup = Project()

        # create TA first
        mySetup.command("login King password1")
        mySetup.command("user add perms=TA username=Lars password=password2")
        mySetup.command("logout")

        # TA edits phone number
        mySetup.command("login Lars password2")
        self.assertEqual(mySetup.command("user edit phone=(414)883-4893"),
                         "Lars successfully changed phone number to (414)883-4893",
                         "Test failed. Unable to edit phone number")
        mySetup.command("logout")


class TestSupervisor(unittest.TestCase):

    # Test #24 Create account
    def createNoLoggin(self):

        mySetup = Project()

        self.assertEqual(mySetup.command("user add perms=student username=Momo password=Cram"),
                         "You need to login before you can edit contact information",
                         "Test failed. Should not have been able to create account without logging in")

    # Test if create user fails if they are not given a role
    def createNoRole(self):

        mySetup = Project()
        mySetup.command("login King password1")
        self.assertEqual(mySetup.command("user add username=Momo password=Cram"),
                         "You need to assign a role to the new user",
                         "Test failed. Should not have been able to add user without a role")
        mySetup.command("logout")

    # No password
    def createNoPass(self):

        mySetup = Project()
        mySetup.command("user login King")
        self.assertEqual(mySetup.command("user add perms=student username=Momo"),
                         "You need to assign a password to the new user",
                         "Test failed. Should not have been able to add user without a role")
        mySetup.command("logout")

    # No username
    def createNoUsername(self):
        mySetup = Project()
        mySetup.command("user login King")
        self.assertEqual(mySetup.command("user add perms=student password=Hello"),
                         "You need to assign a password to the new user",
                         "Test failed. Should not have been able to add user without a role")
        mySetup.command("logout")

        # Test a successful add for each role
    def createUserSuccess(self):
        mySetup = Project()
        mySetup.command("login King")
        self.assertEqual(mySetup.command("user add perms=student username=Momo password=Cram"),
                         "Momo successfully added", "user was not successfully added")
        mySetup.command("logout")

    # user adding account is not a supervisor
    def createNotSupervisor(self):

        mySetup = Project()

        mySetup.command("user login Momo")
        self.assertEqual(mySetup.command("user add perms=student username=Tom password=Cream"), "Nono can't add users",
                         "Test Failed. This user should not be able to add users")
        mySetup.command("logout")

    # Add course #22
    # Test to make sure Supervisor is logged in
    def courseCorrectLogin(self):

        mySetup = Project()

        # Test no login
        self.assertEqual(mySetup.command("course add CS-251"),
                         "You need to login before you can create a course",
                         "Test failed. Should not have been able to create a course without logging in")

        # Test when student logs in
        mySetup.command("login Mono Cram")
        self.assertEqual(mySetup.command("course add CS-251"),
                         "User not authorized to add course", "Test Failed. Student should not be able to add courses")
        mySetup.command("logout")

    def courseSuccessAdd(self):
        mySetup = Project()
        mySetup.command("login King password1")
        self.assertEqual(mySetup.command("course add CS-251"),
                         "Course Added: CS-251", "Test Failed. Course was not successfully added")
        mySetup.command("logout")


    # account edit by supervisor #30
    def accountEdit(self):
        mySetup = Project()

        # Test no login
        self.assertEqual(mySetup.command("user edit Nono role=TA"),
                         "You need to login before you can edit a user",
                         "Test failed. Should not have been able to edit user without logging in")
        # Test student login
        mySetup.command("login Mono Cram")
        self.assertEqual(mySetup.command("user edit King role=TA"),
                         "User not authorized to change role", "Test Failed. Student should not be able to edit roles")
        mySetup.command("logout")

        mySetup.command("login King password1")
        self.assertEqual(mySetup.command("user edit Mono role=TA"),
                         "Successfully changed Mono role to TA", "Test Failed. Role was not successfully changed")

    # Test different account changes
    def accountChanges(self):
        mySetup = Project()

        mySetup.command("login King password1")
        self.assertEqual(mySetup.command("user edit Lars officehrs=9:00AM-10:30AM"),
                         "Lars office hours successfully changed",
                         "Test Failed. Nono should have been changed to TA")
        mySetup.command("logout")

    # Test delete with supervisor #31
    def deleteAccount(self):
        mySetup = Project()

        mySetup.command("login King password1")
        self.assertEqual(mySetup.command("user delete Lars"), "User successfully removed",
                         "User could not be removed successfully")
        mySetup.command("logout")


# Test that any user's ability to view a specific course #99
class TestAll(unittest.TestCase):

    def userLoggedIn(self):
        mySetup = Project()

        # Test to make sure user is logged in
        self.assertEqual(mySetup.command("course view CS-417"),
                         "You need to login before you can create a course",
                         "Test failed. Should not have been able to create a course without logging in")

    # create course and test view with supervisor
    def successView(self):
        mySetup = Project()

        mySetup.command("login King password1")
        mySetup.command("course add CS-417")
        self.assertEqual(mySetup.command("course view CS-417"),
                         "Course: CS-417\nSections: None\nInstructor: None\nTA: None, ",
                         "Test failed. Course could not be viewed by Supervisor")

        # add users for next tests
        mySetup.command("user add perms=TA username=Lars password=password2")
        mySetup.command("user add perms=administrator username=Sec password=password3")
        mySetup.command("user add perms=student username=Momo password=Cram")
        mySetup.command("user logout King")

        # Test view with TA
        mySetup.command("login Lars password2")
        self.assertEqual(mySetup.command("course view CS-417"),
                         "Course: CS-417\nSections: None\nInstructor: None\nTA: None, ",
                         "Test failed. Course could not be viewed by TA")
        mySetup.command("user logout Lars")

        # Test view with Student
        mySetup.command("login Momo Cram")
        self.assertEqual(mySetup.command("course view CS-417"),
                         "Course: CS-417\nSections: None\nInstructor: None\nTA: None, ",
                         "Test failed. Course could not be viewed by Student")
        mySetup.command("logout")

        # Test view with Administrator
        mySetup.command("login Sec password3")
        self.assertEqual(mySetup.command("course view CS-417"),
                         "Course: CS-417\nSections: None\nInstructor: None\nTA: None, ",
                         "Test failed. Course could not be viewed by Administrator")
        mySetup.command("logout")


