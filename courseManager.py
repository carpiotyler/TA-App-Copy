from StorageManager.JSONStorageManager import JSONStorageManager
from sectionManager import mySectionManager

# Course obj used for CourseManger, might place in seperate file once we finalize everything
class Course:
    
    def __init__(self,dept,cnum,ta):
        self.dept = dept
        self.cnum = cnum
        self.ta = ta
        
# Handles adding,viewing,editing and deleting of all courses.
class CourseManager:

    # Right now only CS dept courses can be added with manager. Dept list can be changed to support more departments
    depts = ['CS']
    c = None    
    s = JSONStorageManager()
    sec = mySectionManager()
    

    # Adds course to database using database manager and section manager
    def add(self, dept=None, cnum=None, ta=None, section=None, instr=None):

        # Both dept and cnum are mandatory in order to add course
        if dept is None: raise ValueError ("Dept not specified")
        if cnum is None: raise ValueError ("Cnum not specified")
    
        dept = dept.upper()

        # Messy if statements, need to get refactored in next commit
        if dept in self.depts: 
            if cnum.isdigit():
                if isinstance(ta,str):
                    c = Course(dept,cnum,ta)
                    self.s.insert_course(c)
                else:
                    c = Course(dept,cnum,None)
                    self.s.insert_course(c)
        else: raise ValueError ("Invalid dept.")

        # If parser provides section, call the section manager to add it.
        if section!=None:
            self.sec.add(dept,cnum,section,instr)
    
    # Get course from database manager to pass back to the parser in order to print
    # Will need to change depending on the format that the parser requires
    def view(self, dept=None, cnum=None, ta=None, section=None, instr=None):
       
        if dept is None: raise ValueError ("Dept not specified")
        if cnum is None: raise ValueError ("Cnum not specified")
        self.s.get_course(dept,cnum)

    def delete(self,dept=None, cnum=None, ta=None, section=None, instr=None):
        pass

    def edit(self,dept=None, cnum=None, ta=None, section=None, instr=None):
        pass
        