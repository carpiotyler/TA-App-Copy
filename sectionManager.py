

class sectionManager:

    # validates and adds to database if okay
    def add(self, dept, cnum, snum):
        pass

    # validates and deletes from database
    def delete(self, dept, cnum, snum):
        pass

    # validates and copies information from database to report
    def view(self, dept, cnum, snum):
        pass

    # validates and takes given section and edits what is asked to edit
    def edit(self, dept, cnum, snum):
        pass

    # retrieve other sections associated with this one
    def getAssociated(self, dept, cnum, snum):
        pass

    # get associated instructor/TA
    def getInstructor(self, dept, cnum, snum):
        pass
