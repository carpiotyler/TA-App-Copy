class Course:

    def __init__(self, str_dept, str_cnum, strarray_sections=[], str_name="", str_description=""):
        self.dept = str_dept
        self.cnum = str_cnum
        self.sections = strarray_sections
        self.name = str_name
        self.description = str_description