# import databaseManager

class Section:

    def __init__(self, dept, course, snum):
        self.department = dept
        self.course = course
        self.sectionNum = snum

    def getDepartment(self):
        return self.department

    def getCourse(self):
        return self.course

    def getSectionNum(self):
        return self.sectionNum

    def setDepartment(self, dept):
        self.department = dept

    def setCourse(self, course):
        self.course = course

    def setSectionNum(self, snum):
        self.sectionNum = snum

    # validates and adds to database if okay
    def add(self):
        if self.exists():
            return "Section already exists"
        pass

    # validates and deletes from database
    def delete(self):
        pass

    # validates and copies information from database to report
    def view(self):
        pass

    # validates and takes given section and edits what is asked to edit
    def edit(self):
        pass


    # helper used to get sections associated with this within the course
    # for making sure sections being added don't already exist
    # and that adding/editing a section does not create time conflicts
    # get sections directly associated with this section
    def getAssociated(self, snum, course, department):
        pass

    # get associated instructor/TA
    # helper is used to make sure adding a TA/instructor to a section doesn't create a conflict
    def getInstructor(self, snum, course, department):
        pass

    # check if number format is correct (e.g. labs should be 801, discussions 601, lectures 401)
    def valNum(self):
        pass

    # make sure lectures don't conflict with discussion/lab times
    def valTime(self):
        pass

    # make sure the person being assigned to a section's time doesn't conflict when added or edited
    def valUserSchedule(self):
        pass

    # return true if section already exists for this course
    def exists(self):
        return False
