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

        dept = fields.get('dept').upper()
        cnum = fields.get('cnum')
        section = fields.get('section')
        descr = fields.get('description')
        name = fields.get('name')

        # Checks if dept isvalid
        if dept in self.depts:

            # If sections is passed, call section manager to add section
            if section is None:
                c = Course(dept=dept, cnum=cnum, description=descr, name=name)
                return dm.insert_course(c)

            c = Course(dept=dept, cnum=cnum, description=descr, name=name)
            dm.insert_course(c)
            
            if self.sec.add(fields):
                return True
            dm.delete(c)

        return False

    def view(self, fields: dict):
        """Get courselist from db manager, convert to string and pass back to parser"""

        dept = fields.get('dept').upper()
        cnum = fields.get('cnum')

        # View all courses
        if not dept and not cnum:
            courselist = dm.get_courses_by(dept="", cnum="")
            return self._courselist_string(courselist)
        # View by dept
        elif dept and not cnum:
            courselist = dm.get_courses_by(dept=dept)
            return self._courselist_string(courselist)

        # View single course
        else:
            course_list = dm.get_courses_by(dept=dept, cnum=cnum)
            return self._courselist_string(courselist)

    def delete(self, fields: dict):
        """Delete a specific course from the database"""

        if not self._check_params(fields):
            return False

        dept = fields.get('dept').upper()
        cnum = fields.get('cnum')
        section = fields.get('section')

        if section:
            return self.sec.delete(fields)
        course_list = dm.get_courses_by(dept=dept, cnum=cnum)
        
        for c in course_list:
            if not dm.delete(c):
                return False
        return True

        

    def edit(self, fields: dict):

        if self._check_params(fields):
            c = dm.get_course(dept=fields['dept'], cnum=fields['cnum'])
            c.cnum = fields['cnum']
            c.dept = fields['dept']
        if 'name' in fields:
            c.name = fields['name']
        if 'description' in fields:
            c.description = fields['description']
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
    def _courselist_string(self, courselist):

        if not courselist:
            return 'No course found in database.'

        coursestring = ''
        for c in courselist:
            coursestring = coursestring + str(c)+ '\n'
        return coursestring

    # @static
    # def reqFields()->list:
    #     pass

    # @static
    # def optFields()->list:
    #     pass
