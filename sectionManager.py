from StorageManager import JSONStorageManager as jsm
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


    # validates and adds to database if okay
    def add(self, dept=None, cnum=None, snum=None, ins=None):

        """Don't know what file to write to"""
        db = jsm.JSONStorageManager("section.json")

        # check if user inputs information needed for adding
        invalid = self.actionHelper(dept, cnum, snum, "addition")
        if invalid != "okay":
            return invalid
        if self.exists(db, dept, cnum, snum):
            return "Section already exists"

        sec = Section(dept, cnum, snum)
        db.insert_section(sec)

        """Do you prefer to create a string prior to return or is this okay?"""
        return "Section Added: " + sec.toString()

    # validates and deletes from database
    def delete(self, dept=None, cnum=None, snum=None, ins=None):
        pass

    # validates and copies information from database to report
    def view(self, dept=None, cnum=None, snum=None, ins=None):

        """check if user has input enough information"""
        invalid = self.actionHelper(dept, cnum, snum, "view")
        if invalid != "okay":
            return invalid

        """Check if """
        db = jsm.JSONStorageManager("section.json")
        result = db.get_section(dept, cnum, snum)
        if result is None:
            return "Could not find" + dept + "-" + cnum + "-" + snum
        else:
            return result.toString()

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


class Section:

    def __init__(self, dept=None, cnum=None, snum=None):
        self.department = dept
        self.courseNum = cnum
        self.sectionNum = snum

    def getDepartment(self):
        return self.department

    def getCourse(self):
        return self.courseNum

    def getSectionNum(self):
        return self.sectionNum

    def setDepartment(self, dept):
        self.department = dept

    def setCourse(self, course):
        self.courseNum = course

    def setSectionNum(self, snum):
        self.sectionNum = snum

    def toString(self):
        return self.department + "-" + self.courseNum + "-" + self.sectionNum