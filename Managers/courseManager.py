from Managers.sectionManager import SectionManager
from Managers.DjangoStorageManager import DjangoStorageManager as dm
from TAServer.models import Course

# Course obj used for CourseManger, might place in seperate file once we finalize everything

        
# Handles adding,viewing,editing and deleting of all courses.
class CourseManager:

    def __init__(self):

        # Right now only CS dept courses can be added with manager. 
        # Dept list can be changed to support more departments
        self.reqFields = ['dept', 'cnum']
        self.optFields = ['name', 'description', 'section', 'instr']
        self.depts = ['CS']
        self.sec = SectionManager()
        dm.set_up(overwrite=False)


    def add(self, fields: dict):
        """Adds course to database using database manager and section manager"""

        # Both dept and cnum are mandatory in order to add course
        if not self._check_params(fields):
            return False

        # Storing dict values into variables
        dept = fields.get('dept').upper()
        cnum = fields.get('cnum')
        section = fields.get('section')
        descr = fields.get('description')
        name = fields.get('name')

        # Checks if dept isvalid
        if dept in self.depts:

            # Create course objecte with given fields
            c = Course(dept=dept, cnum=cnum, description=descr, name=name)

            # If sections is None, just call database manager to add course
            if section is None:
                return dm.insert_course(c)

            # Else insert course
            dm.insert_course(c)
            
            # Call section manager to add section, if section created successfully, return True,
            # else delete course and return False
            if self.sec.add(fields):
                return True
            dm.delete(c)

        return False

    def view(self, fields: dict):
        """Get course list from db manager, convert to string and pass back to parser"""

        # Store dict values into variables
        dept = fields.get('dept').upper()
        cnum = fields.get('cnum')

        # View all courses
        if not dept and not cnum:
            course_list = dm.get_courses_by(dept="", cnum="")
            return self._course_list_string(course_list)

        # View by dept
        elif dept and not cnum:
            course_list = dm.get_courses_by(dept=dept)
            return self._course_list_string(course_list)

        # View single course
        else:
            course_list = dm.get_courses_by(dept=dept, cnum=cnum)
            return self._course_list_string(course_list)

    def delete(self, fields: dict):
        """Delete a specific course from the database"""

        # Check if required params are present and error check optional params
        if not self._check_params(fields):
            return False

        # Store dict values into variables
        dept = fields.get('dept').upper()
        cnum = fields.get('cnum')
        section = fields.get('section')

        # Delete section only
        if section:
            return self.sec.delete(fields)

        # Retrieve courses with dept and cnum
        course_list = dm.get_courses_by(dept=dept, cnum=cnum)
        
        # Delete all courses retreived from database with given dept and cnum
        for c in course_list:
            if not dm.delete(c):
                return False
        return True

        

    def edit(self, fields: dict):
        '''Edit a specific course in the database'''
        
        # Check if required fields are present and error check optional fields
        if self._check_params(fields):

            # Get course to edit
            c = dm.get_course(dept=fields['dept'], cnum=fields['cnum'])

            # Edit name
            if 'name' in fields:
                c.name = fields['name']

            # Edit description
            if 'description' in fields:
                c.description = fields['description']

            # Edit sections, insert course with database manager and have section manager edit sections
            if 'sections' in fields:
                if dm.insert_course(c):
                    return self.sec.edit(fields)
                return False

        return dm.insert_course(c)

    # Check for invalid parameters
    def _check_params(self, fields: dict):

        dept = fields.get('dept')
        cnum = fields.get('cnum')
        section = fields.get('section')
        instr = fields.get('instr')

        if not dept:
            return False

        if not cnum:
            return False

        if not cnum.isdigit():
            return False

        if instr:
            if not all(x.isalpha() or x.isspace() for x in instr):
                return False

        if instr and not section:
            return False

        else: return True
    
    # Converts list of courses into a printable string
    def _course_list_string(self, course_list):

        if not course_list:
            return 'No course found in database.'

        coursestring = ''
        for c in course_list:
            coursestring = coursestring + str(c)+ '\n'
        return coursestring

    # @static
    # def reqFields()->list:
    #     pass

    # @static
    # def optFields()->list:
    #     pass
