from JSONStorageManager import JSONStorageManager as jsm
import abc


class SectionManager(abc.ABC):

    # validates and adds to database if okay
    def add(self, dept=None, cnum=None, snum=None, ins=None):
        pass

    # validates and deletes from database
    def delete(self, dept=None, cnum=None, snum=None, ins=None):
        pass

    # validates and copies information from database to report
    def view(self, dept=None, cnum=None, snum=None, ins=None):
        pass

    # validates and takes given section and edits what is asked to edit
    def edit(self, dept=None, cnum=None, snum=None, ins=None):
        pass

class mySectionManager(SectionManager):

    def __init__(self):
        self.db = jsm("section.json")

    # validates and adds to database if okay
    def add(self, dept=None, cnum=None, snum=None, ins=None):

        # check if user inputs information needed for adding
        invalid = self.actionHelper(dept, cnum, snum, "addition")
        if invalid != "okay":
            return invalid
        if self.exists(self.db, dept, cnum, snum):
            return "Section already exists"
        if not self.userExist(ins):
            return ins + " does not exist in the system"

        sec = self.db.Section(dept, cnum, snum)
        self.db.insert_section(sec)

        return "Section Added: " + dept + "-" + cnum + "-" + snum + "instructor= " + ins

    # validates and deletes from database
    def delete(self, dept=None, cnum=None, snum=None, ins=None):
        pass

    # validates and copies information from database to report
    def view(self, dept=None, cnum=None, snum=None, ins=None):

        """check if user has input enough information"""
        invalid = self.actionHelper(dept, cnum, snum, "view")
        if invalid != "okay":
            return invalid

        """Check if Section exists in the database and return"""

        result = self.db.get_section(dept, cnum, snum)
        if result is None:
            return "Could not find" + dept + "-" + cnum + "-" + snum
        else:
            return result.dept + "-" + result.cnum + "-" + result.snum + "instructor= " + result.instructor

    # validates and takes given section and edits what is asked to edit
    def edit(self, dept=None, cnum=None, snum=None, ins=None):
        pass

    # make sure necessary fields are not set to None
    def actionHelper(self, dept, cnum, snum, action):
        okay = ""
        switch = {
            dept: "Could not complete " + action + ", department is needed",
            cnum: "Could not complete " + action + ", course number is needed",
            snum: "Could not complete " + action + ", section number is needed"
        }
        return switch.get(None, "okay")

    # check if number format is correct (e.g. labs should be 801, discussions 601, lectures 401)
    """Specific requirements for section numbers aren't implemented yet"""
    def valNum(self):
        pass

    # make sure lectures don't conflict with discussion/lab times
    """Times aren't implemented yet"""
    def valTime(self):
        pass

    # make sure the person being assigned to a section's time doesn't conflict when added or edited
    """times aren't implemented yet"""
    def valUserSchedule(self):
        pass

    # return true if section already exists for this course
    def exists(self, db, dept, cnum, snum):
        retrieved = db.get_section(dept, cnum, snum)
        if retrieved is None:
            return False
        else:
            return True

    def userExist(self, ins):
        if self.db.get_user(ins) is None:
            return False
        else:
            return True
