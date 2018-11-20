class Section:

    def __init__(self, str_dept, str_cnum, str_snum, str_instructor="", type=None, days=None, room=None, time=None):
        self.dept = str_dept
        self.cnum = str_cnum
        self.snum = str_snum
        self.instructor = str_instructor
        self.type = type
        self.days = days
        self.room = room
        self.time = time