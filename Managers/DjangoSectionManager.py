from Managers.DjangoStorageManager import DjangoStorageManager as dsm
from Managers.managerInterface import ManagerInterface
from Domain.section import Section
from TAServer.models import Section


class SectionManager(ManagerInterface):

    def __init__(self, db : dsm):
        self.db = db

    def add(self, fields: dict)->bool:

        # check if user inputs information needed for adding
        invalid = self.actionHelper(fields.get("dept"), fields.get("cnum"), fields.get("snum"), "addition")
        if invalid != "okay":
            print(invalid)
            return False

        toAdd = Section(str_dept=fields.get("dept"),str_cnum=fields.get("cnum"),str_snum=fields.get("snum"),
                        str_instructor=fields.get("instructor"), type=fields.get("type"), days=fields.get("days"),
                        room=fields.get("room"), endTime=fields.get("endTime"), startTime=fields.get("startTime"))

        # Make sure course already exists
        if not self.courseExists(cnum=toAdd.cnum, dept=toAdd.dept):
            return False

        # Make sure user exists if inst is to be added
        if toAdd.instructor is not None and not self.userExists(toAdd.instructor):
            return False

        # Check for correct time format of start and end time
        if not self.timeFormat(toAdd.startTime) or not self.timeFormat(toAdd.endTime):
            return False

        # Check if time and room conflict
        if not self.roomConflict(start=toAdd.startTime, end=toAdd.endTime, room=toAdd.room):
            return False

        # With and without instructor adding to course and sections db
        if toAdd.instructor is None:
            toAdd.instructor = #TODO: add empty instructor
            self.addHelper(toAdd)
            return True
        else:
            if not self.valUser(toAdd.instructor):
                return False
            self.addHelper(toAdd)
            return True



    def view(self, fields: dict)->str:

        invalid = self.actionHelper(fields.get("dept"), fields.get("cnum"), fields.get("snum"), "viewing")
        if invalid != "okay":
            return invalid

        result = self.db.get_section(dept = fields.get("dept"), cnum = fields.get("cnum"), snum = fields.get("snum"))
        if result is None:
            return "Could not find " + fields.get("dept") + "-" + fields.get("cnum") + "-" + fields.get("snum")
        else:
            return "Course: " + result.dept + "-" + result.cnum + "<br>Section: " + result.snum \
                   + "<br>Instructor: " + result.instructor + "<br>Meeting time(s): " + result.days + " " + result.time

    # Edit will need cnum, snum and dept (like all other commands)
    # Any other fields specified that aren't above(e.g. room, instructor, ect.) will replace what is already in the section
    # You can not change cnum and dept, but if you want to change snum use key "snumNew" as a replacement
    def edit(self, fields: dict)->bool:
        invalid = self.actionHelper(fields.get("dept"), fields.get("cnum"), fields.get("snum"), "editing")
        if invalid != "okay":
            print(invalid)
            return False

        toEdit = Section(str_dept=fields.get("dept"), str_cnum=fields.get("cnum"), str_snum=fields.get("snum"),
                        str_instructor=fields.get("instructor"), type=fields.get("type"), days=fields.get("days"),
                        room=fields.get("room"), endTime=fields.get("endTime"), startTime=fields.get("startTime"))

        # Make sure course already exists
        if not self.courseExists(cnum=toEdit.cnum, dept=toEdit.dept):
            return False

        # Make sure user exists if inst is to be added
        if toEdit.instructor is not None and not self.userExists(toEdit.instructor):
            return False

        # Check for correct time format of start and end time
        if not self.timeFormat(toEdit.startTime) or not self.timeFormat(toEdit.endTime):
            return False

        # Check if time and room conflict
        if not self.roomConflict(start=toEdit.startTime, end=toEdit.endTime, room=toEdit.room):
            return False

        # With and without instructor adding to course and sections db
        if toEdit.instructor is None:
            toEdit.instructor = #TODO: add empty instructor
            self.addHelper(toEdit)
            return True
        else:
            if not self.valUser(toEdit.instructor):
                return False
            self.addHelper(toEdit)
            return True

    def delete(self, fields: dict)->bool:

        invalid = self.actionHelper(fields.get("dept"), fields.get("cnum"), fields.get("snum"), "deletion")
        if invalid != "okay":
            print(invalid)
            return False

        toDel = Section(str_dept=fields.get("dept"),str_cnum=fields.get("cnum"),str_snum=fields.get("snum"),
                        str_instructor=fields.get("instructor"), type=fields.get("type"), days=fields.get("days"),
                        room=fields.get("room"), time=fields.get("time"))

        if self.courseExists(cnum=fields.get("cnum"), dept=fields.get("dept")):
            self.db.delete(toDel)
            return True
        else:
            return False

    # Make sure user exists
    def userExists(self, ins):
        user = self.db.get_user(ins)
        return user is not None

    # Make sure course exists
    def courseExists(self, cnum, dept):
        course = self.db.get_course(cnum, dept)
        return course is not None

    # make sure necessary fields are not set to None
    def actionHelper(self, dept, cnum, snum, action):
        okay = ""
        switch = {
            dept: "Could not complete " + action + ", department is needed",
            cnum: "Could not complete " + action + ", course number is needed",
            snum: "Could not complete " + action + ", section number is needed"
        }
        return switch.get(None, "okay")

    def addHelper(self, sec: Section):
        self.db.insert_section(sec)
        course = self.db.get_course(sec.dept, sec.cnum)
        if sec.snum not in course.sections:
            course.sections.append(sec.snum)
        self.db.insert_course(course)

    # Make sure user is a TA or instructor
    #TODO: make sure to allow empty user object for a "placeholder"
    def valUser(self, ins):
        user = self.db.get_user(ins)
        if user.role.lower() != "ta" and user.role.lower() != "instructor":
            return False
        else:
            return True

    # check the time input to make sure it's in the correct format 12:20 PM
    def timeFormat(self, time : str)->bool:
        #Note: strip string before passing
        if time is None:
            return True
        broken = time.split(" ")
        if len(broken) is not 2:
            return False
        minHr = broken[0].split(":")
        min = minHr[0]
        Hr = minHr[1]
        #check if min has  2 characters (1:5 pm or 1:0 pm will not be accepted) and hr has at least one but not more than 2 (01:30 or 1:30 is fine)
        if len(min) != 2 or len(Hr) > 2 or len(Hr) < 1:
            return False

        # try to convert two strings into integers (minute and hour)
        try:
            min = int(min)
            Hr = int(Hr)
        except ValueError:
            print ('Time is not a valid integer')
            return False

       # for min and Hr, check appropriate range
        if min < 0 or min >= 60:
            return False
        if Hr < 1 or Hr > 12:
            return False

        # check if the second half of the original split string broken[1] should be
        # either am or pm (lower case)
        partDay = broken[1].lower()
        if partDay is not "am" or "pm":
            return False
        else:
            return True

    # This helper will take a time in string format and return a integer time
    # The integer will be in military hours for easy comparison in roomConflict()
    # NOTE: time format should be called before calling this method or else int() conversion will fail
    def intTime(self, time : str)->int:

        breakDown = time.split(" ")
        meridies = breakDown[1]
        minHr = breakDown[0].split(":")
        hr = int(minHr[0])
        min = int(minHr[1])

        # convert to military time
        if meridies.lower() is "pm" and hr != 12:
            hr = hr + 12
        elif meridies.lower() is "am" and hr == 12:
            hr = 0
        hr = str(hr)
        min = str(min)
        intTime = hr + min
        intTime = int(intTime)
        return intTime

    # NOTE: timeFormat() should be called before calling this method
    def roomConflict(self, start: str, end: str, room: int)->bool:

        if start is None or room is None or end is None:
            return True

        roomUse = Section.objects.filter(room=room)
        if roomUse.count() > 0:

            # get integer values for start and end times for comparison
            startTime = self.intTime(start)
            endTime = self.intTime(end)

            for x in roomUse:
                xStart = self.intTime(x.startTime)
                xEnd = self.intTime(x.endTime)

                # check if start and end time is between each other class that shares the same room
                if xStart <= startTime <= xEnd:
                    return False
                elif xStart <= endTime <= xEnd:
                    return False

        return True

    @static
    def reqFields(self)->list:
        return ["dept", "cnum", "snum"]

    @static
    def optFields(self)->list:
        return ["instructor", "type", "days", "room", "startTime", "endTime"]