from StorageManager.JSONStorageManager import JSONStorageManager
from sectionManager import mySectionManager

class Course:
    
    def __init__(self,dept,cnum,ta,section):
        self.dept = dept
        self.cnum = cnum
        self.ta = ta
        self.section = section
        

class CourseManager:

    depts = ['CS']
    c = None
    s = JSONStorageManager()
    sec = mySectionManager()
    

    def add(self, dept=None, cnum=None, ta=None, section=None, instr=None):
        pass
    
    def view(self, dept=None, cnum=None, ta=None, section=None, instr=None):
        pass

    def delete(self,dept=None, cnum=None, ta=None, section=None, instr=None):
        pass

    def edit(self,dept=None, cnum=None, ta=None, section=None, instr=None):
        pass
        
  