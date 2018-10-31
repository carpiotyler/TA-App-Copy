

class sectionManager:

    # validates and adds to database if okay
    def add(self):
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

    # retrieve other sections associated with this one
    def getAssociated(self, snum, course, department):
        pass

    # get associated instructor/TA
    def getInstructor(self, snum, course, department):
        pass

    def getDepartment(self):
        pass

    def getCourse(self):
        pass

    def getSectionNum(self):
        pass

    def setDepartment(self, dept):
        pass

    def setCourse(self, course):
        pass

    def setSectionNum(self, snum):
        pass