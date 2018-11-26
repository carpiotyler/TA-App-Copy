# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.db import models
from django.contrib.auth.models import User, Group

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
        ('lecture', 'Lecture'),
        ('None', 'Unassigned')
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
        ('MWF', "Monday Wednesday Friday"),
        ('None', "Unassigned")
    )
    # section number
    snum = models.CharField(max_length=4)
    # section type (uses SEC_TYPE)
    stype = models.CharField(max_length=10, choices=SEC_TYPE, blank=True, null=True)
    # course points to course model
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # room Number
    room = models.IntegerField(default=-1, blank=True, null=True)
    # instructor or ta
    instructor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    # days of week meeting
    days = models.CharField(max_length=5, choices=DAYS, default='None')
    # time of meeting ("05:45 AM" or "5:45 PM")
    startTime = models.CharField(max_length=8, blank=True)
    # time of meeting end
    endTime = models.CharField(max_length=8, blank=True)

class Staff(User):
    ROLES = (
        ('T', 'TA'),
        ('I', 'Instructor'),
        ('A', 'Administrator'),
        ('S', 'Supervisor'),
        ('None', 'Unassigned')
    )

    role = models.CharField(max_length=13, choices=ROLES, default="None")
    sections = models.ManyToManyField(Section, blank=True) # For TA's
    courses = models.ManyToManyField(Course, blank=True) # For instructors
    phonenum = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=30, default="")
