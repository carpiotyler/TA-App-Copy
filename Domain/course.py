class Course:

    def __init__(self, str_dept, str_cnum, strarray_sections=[], str_name="", str_description=""):
        self.dept = str_dept
        self.cnum = str_cnum
        self.sections = strarray_sections
        self.name = str_name
        self.description = str_description

    def __str__(self):
        return "Department: %s\nCourse Number: %s\nSections: %s\nCourse Name: %s\nDescription: %s\n" % (self.dept, self.cnum, self.sections, self. name, self.description)
