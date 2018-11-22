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


        pass

    def delete(self, fields: dict)->bool:

        invalid = self.actionHelper(fields.get("dept"), fields.get("cnum"), fields.get("snum"), "deletion")
        if invalid != "okay":
            print(invalid)
            return False

        toDel = Section(str_dept=fields.get("dept"),str_cnum=fields.get("cnum"),str_snum=fields.get("snum"),
                        str_instructor=fields.get("instructor"), type=fields.get("type"), days=fields.get("days"),
                        room=fields.get("room"), time=fields.get("time"))
        pass

    # Make sure user exists
    def userExists(self, ins):
        user = self.db.get_user(ins)
        return user is not None

    # make sure necessary fields are not set to None
    def actionHelper(self, dept, cnum, snum, action):
        okay = ""
        switch = {
            dept: "Could not complete " + action + ", department is needed",
            cnum: "Could not complete " + action + ", course number is needed",
            snum: "Could not complete " + action + ", section number is needed"
        }
        return switch.get(None, "okay")

    def addHelper(self, sec : Section):
        self.db.insert_section(sec)
        course = self.db.get_course(sec.dept, sec.cnum)
        if sec.snum not in course.sections:
            course.sections.append(sec.snum)
        self.db.insert_course(course)

    # Make sure user is a TA or instructor
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
        #check if min has  2 char and hr has at least one but not more than 2
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
        if min < 0 or min > 60:
            return False
        if Hr < 1 or Hr > 12:
            return False

        # check if the second half of the original split string broken[1] should be
        # either am or pm
        partDay = broken[1].lower()
        if partDay is not "am" or "pm":
            return False
        else:
            return True

    # This helper will take a time in string format and return a list
    # The list will be [Hour, minutes, meridies] (e.g. 4:30 PM will return [4, 30, "PM"]
    # NOTE: time format should be called before calling this method
    def intTime(self, time : str)->list:

        breakDown = time.split(" ")
        meridies = breakDown[1]
        minHr = breakDown[0].split(":")
        hr = int(minHr[0])
        min = int(minHr[1])
        intTime = [hr, min, meridies]

    # NOTE: time format should be called before calling this method
    def roomConflict(self, start : str, end : str, room: int):

        if start is None or room is None or end is None:
            return True

        breakStart = self.intTime(start)
        startHr = breakStart[0]
        startMin = breakStart[1]
        startMeridies = breakStart[2]

        breakEnd = self.intTime(end)
        endHr = breakEnd[0]
        endMin = breakEnd[1]
        endMeridies = breakEnd[2]

        roomUse = Section.objects.filter(room=room)
        if roomUse.count() > 0:
            for x in roomUse:
                breakStart = x.startTime.split(" ")
                xStartMeridies = breakStart[1]
                minHr = breakStart[0].split(":")
                xStartMin = minHr[1]
                xStartHr = minHr[0]

                breakEnd = x.endTime.split(" ")
                xEndMeridies = breakEnd[1]
                minHr = breakEnd[0].split(":")
                xEndMin = minHr[1]
                xEndHr = minHr[0]
                if


    @static
    def reqFields(self)->list:
        return ["dept", "cnum", "snum"]

    @static
    def optFields(self)->list:
        return ["instructor", "type", "days", "room", "startTime", "endTime"]