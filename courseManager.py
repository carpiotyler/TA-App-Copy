from Managers.JSONStorageManager import JSONStorageManager
from Managers.myStorageManager import AbstractStorageManager as storage
from Managers.sectionManager import SectionManager

# Course obj used for CourseManger, might place in seperate file once we finalize everything

        
# Handles adding,viewing,editing and deleting of all courses.
class CourseManager:

    # Right now only CS dept courses can be added with manager. Dept list can be changed to support more departments
    depts = ['CS']
    c = None    
    s = JSONStorageManager()
    s.set_up()
    sec = SectionManager()
    

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

            return True

        else: 
#            print("Invalid dept.")
            return False

    
    # Get courselist from db manager, convert to string and pass back to parser
    def view(self, dept=None, cnum=None, instr=None, section=None):

        if not dept and not cnum:
            courselist = self.s.get_course('','')
            return self._courselist_string(courselist)

        elif dept and not cnum:
            courselist = self.s.get_course(dept,'')
            return self._courselist_string(courselist)
            
        else:
            return self.s.get_course(dept,cnum)

    def delete(self,dept=None, cnum=None, instr=None, section=None ):
        pass

    def edit(self,dept=None, cnum=None, instr=None, section=None ):
        pass


    # Check for invalid parameters    
    def _check_params(self=None,dept=None,cnum=None,instr=None,section=None):
        if not dept: 
#            print( "Dept not specified.") 
            return False
        if not cnum: 
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
        else: return True
    
    # Converts list of courses into a printable string
    def _courselist_string(self, courselist):

        coursestring = ''
        for c in courselist:
            coursestring = coursestring + str(c)+ '\n'
        return coursestring
