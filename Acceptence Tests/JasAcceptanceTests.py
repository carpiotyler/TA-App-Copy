import unittest
from skeleton import Project

class TestTA(unittest.TestCase):

    def setUp(self):
        self.p = Project()

        #Setup TA users
        self.p.command("user add perms=TA username=ta1 password=password")
        self.p.command("user add perms=TA username=ta2 password=password email=ta2@uwm.edu pnumber=4142321232 address=123 Maryland Ave")
    def tearDown(self):
        self.p.command("logout")

    # User Story #25 : TA: View TA assignments
    def test_ta_view_ta_assignments(self):
        self.p.command("login supervisor1 password")

        #Add course and assign TAs to sections
        self.p.command("course add dept=CS cnum=351")
        self.p.command("section add dept=CS cnum=351 snum=801")
        self.p.command("section add dept=CS cnum=351 snum=802")
        self.p.command("section edit code=CS-351-801 TA=ta1")
        self.p.command("section edit code=CS-351-802 TA=ta2")
        self.p.command("logout")

        #Login to TA account
        self.p.command("login ta1 password")

        #View assignment of second TA
        self.assertEqual("Course: CS-351 Section:802",self.p.command("user view-assignments ta2"))

    # User Story #34 : TA: Read public contact information for all users
    def test_ta_read_public_info(self):
        self.p.command("login ta1 password")
        
        #Only display public info 
        self.assertEqual("email=ta2@uwm.edu",self.p.command("user view-info ta2"))

class TestInstructor(unittest.TestCase):

    def setUp(self):
        self.p=Project()

        #Create users
        self.p.command("user add perms=INSTRUCTOR username=instr1 password=password")
        self.p.command("user add perms=TA username=ta1 password=password")
        self.p.command("user add perms=TA username=ta2 password=password email=ta2@uwm.edu")

    def tearDown(self):
        self.p.command("logout")

    # User Story #42 : Instructor: View TA assignments
    def test_instr_view_ta_assignments(self):
        self.p.command("login supervisor1 password")

        #Add course and assign TAs to sections
        self.p.command("course add dept=CS cnum=351 instructor=instr1")
        self.p.command("section add dept=CS cnum=351 snum=801")
        self.p.command("section edit code=CS-351-802 TA=ta2")
        self.p.command("logout")

        
        self.p.command("login instr1 password")

        #ta1 should have no assignments, ta2 is assigned to CS-351 Section 802
        self.assertEqual("None","user view-assignments ta1")
        self.assertEqual("Course: CS-351 Section:802","user view-assignments ta2")

    # User Story #43 : Instructor: Get TA email
    def test_instr_view_ta_email(self):
        self.p.command("login instr1 password")
        self.assertEqual("None","user view-info ta1")
        self.assertEqual("Email: ta2@uwm.edu","user view-info ta2")

    # User Story #48 : Change TA lab section
    def test_instr_change_ta_lab(self):
        self.p.command("login supervisor1 password")

        #Add course and assign TAs to sections
        self.p.command("course add dept=CS cnum=351 instructor=instr1")
        self.p.command("section add dept=CS cnum=351 snum=801")
        self.p.command("section add dept=CS cnum=351 snum=802")
        self.p.command("section edit code=CS-351-802 TA=ta2")
        self.p.command("logout")

        
        self.p.command("login instr1 password")

        #Test changes to sections
        self.assertEqual("TA section changed.",self.p.command("user edit ta2 snum=801"))
        self.assertEqual("Course: CS-351 Section:801",self.p.command("user view-assignments ta2"))
        self.assertEqual("TA section changed.",self.p.command("user edit ta2 snum=802"))
        self.assertEqual("Course: CS-351 Section:802",self.p.command("user view-assignments ta2"))