from Managers.sectionManager import SectionManager
from Managers.ManagerInterface import ManagerInterface
from Managers.DjangoStorageManager import DjangoStorageManager as dsm
from TAServer.models import Course

# Course obj used for CourseManger, might place in seperate file once we finalize everything

        
# Handles adding,viewing,editing and deleting of all courses.
class CourseManager(ManagerInterface):

    def __init__(self, dm: dsm):

        # Right now only CS dept courses can be added with manager. 
        # Dept list can be changed to support more departments
        self.depts = ['CS']
        self.dm = dm
        self.sec = SectionManager(self.dm)


    def add(self, fields: dict):
        """Adds course to database using database manager and section manager"""

        # Both dept and cnum are mandatory in order to add course
        if not self._check_params(fields):
            return False

        # Storing dict values into variables
        dept = fields.get('dept').upper()
        cnum = fields.get('cnum')
        snum = fields.get('snum')
        descr = fields.get('description')
        name = fields.get('name')

        # Checks if dept isvalid
        if dept in self.depts:

            # Create course objecte with given fields
            c = Course(dept=dept, cnum=cnum, description=descr, name=name)

            # If sections is None, just call database manager to add course
            if snum is None:
                try:
                    self.dm.insert_course(c)
                    return True
                except:
                    return False

            # Else insert course
            try:
                self.dm.insert_course(c)

                # Call section manager to add section, if section created successfully, return True,
                # else delete course and return False
                if self.sec.add(fields):
                    return True
                self.dm.delete(c)
            except: return False
        return False

    def view(self, fields: dict):
        """Get course list from db manager, convert to string and pass back to parser"""
        dept=None
        cnum=None
        # Store dict values into variables
        if 'dept' in fields:
            dept=fields['dept']
        if 'cnum' in fields:
            dept=fields['cnum']

        # View all courses
        if not dept and not cnum:
            course_list = self.dm.get_courses_by(dept="", cnum="")
            return self._course_list_string(course_list)

        # View by dept
        elif dept and not cnum:
            course_list = self.dm.get_courses_by(dept=dept)
            return self._course_list_string(course_list)

        # View single course
        else:
            course_list = self.dm.get_courses_by(dept=dept, cnum=cnum)
            return self._course_list_string(course_list)

    def delete(self, fields: dict):
        """Delete a specific course from the database"""

        # Check if required params are present and error check optional params
        if not self._check_params(fields):
            return False

        # Store dict values into variables
        dept = fields.get('dept').upper()
        cnum = fields.get('cnum')
        snum = fields.get('snum')

        # Delete section only
        if snum:
            return self.sec.delete(fields)

        # Retrieve courses with dept and cnum
        course_list = self.dm.get_courses_by(dept=dept, cnum=cnum)
        
        # Delete all courses retreived from database with given dept and cnum
        for c in course_list:
            if not self.dm.delete(c):
                return False
        return True

        

    def edit(self, fields: dict):
        '''Edit a specific course in the database'''
        
        # Check if required fields are present and error check optional fields
        if self._check_params(fields):

            # Get course to edit
            c = self.dm.get_course(dept=fields['dept'], cnum=fields['cnum'])

            # Edit name
            if 'name' in fields:
                c.name = fields['name']

            # Edit description
            if 'description' in fields:
                c.description = fields['description']

            # Edit sections, insert course with database manager and have section manager edit sections
            if 'snum' in fields:
                if self.dm.insert_course(c):
                    return self.sec.edit(fields)
                return False

        return self.dm.insert_course(c)

    # Check for invalid parameters
    def _check_params(self, fields: dict):

        dept = fields.get('dept')
        cnum = fields.get('cnum')
        snum = fields.get('snum')
        instructor = fields.get('instructor')

        if not dept:
            return False

        if not cnum:
            return False

        if not cnum.isdigit():
            return False

        if instructor:
            if not all(x.isalpha() or x.isspace() for x in instructor):
                return False

        if instructor and not snum:
            return False

        else: return True
    
    # Converts list of courses into a printable string
    def _course_list_string(self, course_list):
        print(course_list)

        if not course_list:
            return 'No course found in database.'

        coursestring = ''
        for c in course_list:
            coursestring = coursestring + str(c)+ '\n'
        print (coursestring)
        return coursestring

    @staticmethod
    def reqFields()->list:
        return ['dept', 'cnum']
        

    @staticmethod
    def optFields()->list:
        return ['name', 'description', 'snum', 'instructor']
