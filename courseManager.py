from StorageManager.JSONStorageManager import JSONStorageManager
from StorageManager.myStorageManager import AbstractStorageManager as storage
from sectionManager import mySectionManager

# Course obj used for CourseManger, might place in seperate file once we finalize everything

        
# Handles adding,viewing,editing and deleting of all courses.
class CourseManager:

    # Right now only CS dept courses can be added with manager. Dept list can be changed to support more departments
    depts = ['CS']
    c = None    
    s = JSONStorageManager()
    s.set_up()
    sec = mySectionManager()
    

    # Adds course to database using database manager and section manager
    def add(self, dept=None, cnum=None, instr=None, section=None):

        # Both dept and cnum are mandatory in order to add course
        if not self._check_params(dept,cnum,instr,section): return
        dept = dept.upper()

        if dept in self.depts:
            if section is None:
                c = storage.Course(dept,cnum,[],'','')
                self.s.insert_course(c)
            else:
                c = storage.Course(dept,cnum,[],'','')
                self.s.insert_course(c)
                self.sec.add(dept,cnum,section,instr)

        else: 
#            print("Invalid dept.")
            return False
        # If parser provides section, call the section manager to add it.
        if section!=None:
            self.sec.add(dept,cnum,section,instr)
    
    # Get course from database manager to pass back to the parser in order to print
    def view(self, dept=None, cnum=None, instr=None, section=None):
       if self._check_params(dept,cnum):
           return self.s.get_course(dept,cnum)

    def delete(self,dept=None, cnum=None, instr=None, section=None ):
        pass

    def edit(self,dept=None, cnum=None, instr=None, section=None ):
        pass
        
    def _check_params(self=None,dept=None,cnum=None,instr=None,section=None):
        if not dept or None: 
#            print( "Dept not specified.") 
            return False
        if not cnum or None: 
#            print("Cnum not specified.") 
            return False
        if not cnum.isdigit(): 
#            print("Invalid Cnum.") 
            return False
        if instr:
            if not all(x.isalpha() or x.isspace() for x in instr):
#               print("Instructor name should only contain letters.")
                return False
        if instr and not section: 
#            print("Instructor must have section") 
            return False
       