# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2
from django.contrib.auth.models import User, Group
from django.db import models


class TAGroup(Group):
    pass


class InsGroup(Group):
    pass


class AdminGroup(Group):
    pass


class SupGroup(Group):
    pass


class Course(models.Model):
    cnum = models.CharField(max_length = 4, default="")
    name = models.CharField(max_length = 40, default="")
    description = models.CharField(max_length = 200, default="")
    dept = models.CharField(max_length = 10, default="")

    def __str__(self):
        pass

    # returns all sections for course
    def sections (self):
        pass


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
    snum = models.IntegerField()
    # section type (uses SEC_TYPE)
    stype = models.CharField(max_length=10, default="", choices=SEC_TYPE)
    # course points to course model
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    # room Number
    room = models.IntegerField(default=-1)
    # instructor or ta
    instructor = models.ForeignKey(User, blank=True, null=True, on_delete= models.DO_NOTHING)
    # days of week meeting
    days = models.CharField(max_length=5, default="",choices=DAYS)
    # time of meeting ("05:45 AM" or "5:45 PM")
    startTime = models.CharField(max_length=8, default="")
    # time of meeting end
    endTime = models.CharField(max_length=8, default="")


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
