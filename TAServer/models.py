# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2
from django.contrib.auth.models import User, Group
from django.db import models


class DefaultGroup(Group):
    permissions = (("can_view_courses", "Can view courses"),

                   ("can_view_sections", "Can view sections"),

                   ("can_view_user", "Can view users"))


class TAGroup(Group):
    permissions = (("can_view_courses", "Can view courses"),

                   ("can_view_sections", "Can view sections"),

                   ("can_edit_self", "Can edit users"),
                   ("can_view_user", "Can view users"))


class InsGroup(Group):
    permissions = (("can_view_courses", "Can view courses"),

                   ("can_edit_self", "Can edit users"),
                   ("can_view_user", "Can view users"),
                   ("can_view_private", "Can view private user data"),

                   ("can_assign_ta", "Can assign TA's"),

                   ("can_email_tas", "Can send emails"))


class AdminGroup(Group):
    permissions = (("can_create_course", "Can create courses"),
                   ("can_edit_courses", "Can edit courses"),
                   ("can_delete_courses", "Can delete courses"),
                   ("can_view_courses", "Can view courses"),

                   ("can_create_sections", "Can create sections"),
                   ("can_edit_sections", "Can edit sections"),
                   ("can_delete_sections", "Can delete sections"),
                   ("can_view_sections", "Can view sections"),

                   ("can_create_user", "Can create users"),
                   ("can_edit_user", "Can edit users"),
                   ("can_edit_self", "Can edit users"),
                   ("can_delete_user", "Can delete users"),
                   ("can_view_user", "Can view users"),
                   ("can_view_private", "Can view private user data"),

                   ("can_email_all", "Can send emails to all users"))


class SupGroup(Group):
    permissions = (("can_create_course", "Can create courses"),
                   ("can_edit_courses", "Can edit courses"),
                   ("can_delete_courses", "Can delete courses"),
                   ("can_view_courses", "Can view courses"),

                   ("can_create_sections", "Can create sections"),
                   ("can_edit_sections", "Can edit sections"),
                   ("can_delete_sections", "Can delete sections"),
                   ("can_view_sections", "Can view sections"),

                   ("can_create_user", "Can create users"),
                   ("can_edit_user", "Can edit users"),
                   ("can_edit_self", "Can edit users"),
                   ("can_delete_user", "Can delete users"),
                   ("can_view_user", "Can view users"),
                   ("can_view_private", "Can view private user data"),

                   ("can_assign_ta", "Can assign TA's"),
                   ("can_assign_ins", "Can assign instructors"),

                   ("can_email_all", "Can send emails to all users"))


class Course(models.Model):
    cnum = models.CharField(max_length=4)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    dept = models.CharField(max_length=10)
    sections = models.ManyToManyField('Section')

    def __str__(self):
        return "Department: "+ self.dept + " "+"Cnum: "+str(self.cnum) +" "+ "Course Name: "+self.name + '\n' + "Description: " + self.description + '\n' + str(self.sections)



class Section(models.Model):

    # section type
    SEC_TYPE = (
        ('lab', 'Lab'),
        ('lecture', 'Lecture')
    )
    # days to meet (M=Monday, T=Tuesday, W=Wednesday, H=Thursday, F=Friday)
    DAYS = (
        ('M', "Monday"),
        ('T', "Tuesday"),
        ('W', "Wednesday"),
        ('H', "Thursday"),
        ('F', "Friday"),
        ('MW', "Monday Wednesday"),
        ('TH', "Tuesday Thursday"),
        ('MWF', "Monday Wednesday Friday")
    )
    # section number
    snum = models.CharField(max_length=4)
    # section type (uses SEC_TYPE)
    stype = models.CharField(max_length=10, blank=True, null=True, choices=SEC_TYPE)
    # course points to course model
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    # room Number
    room = models.IntegerField(default=-1, blank=True, null=True)
    # instructor or ta
    instructor = models.ForeignKey(User, blank=True, null=True, on_delete= models.DO_NOTHING)
    # days of week meeting
    days = models.CharField(max_length=5, blank=True, null=True, choices=DAYS, default="")
    # time of meeting ("05:45 AM" or "5:45 PM")
    startTime = models.CharField(max_length=8, blank=True, default="")
    # time of meeting end
    endTime = models.CharField(max_length=8, blank=True, default="")

    def __str__(self):
        return "" + self.course.dept + self.course.cnum + self.snum + '\n' + "Section type: " + self.type + '\n' + \
               "room: " + str(self.rooms) + '\n' + "Instructor: " + self.instructor + '\n' + "Time(s) :" + self.days + \
               " " + self.startTime + "-" + self.endTime

class Staff(User):
    ROLES = (
        ('T', 'TA'),
        ('I', 'Instructor'),
        ('A', 'Administrator'),
        ('S', 'Supervisor')
    )

    role = models.CharField(max_length=13, choices=ROLES, default="")
    sections = models.ManyToManyField(Section, blank=True) # For TA's
    courses = models.ManyToManyField(Course, blank=True) # For instructors
    phonenum = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=30, default="")