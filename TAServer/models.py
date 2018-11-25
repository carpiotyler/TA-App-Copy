# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    cnum = models.CharField(max_length = 4)
    name = models.CharField(max_length = 15)
    description = models.CharField(max_length = 75)
    dept = models.CharField(max_length = 10)

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
    stype = models.CharField(max_length=10, choices=SEC_TYPE)
    # course points to course model
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # room Number
    room = models.IntegerField()
    # instructor or ta
    instructor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # days of week meeting
    days = models.CharField(max_length=5, choices=DAYS)
    # time of meeting ("05:45 AM" or "5:45 PM")
    startTime = models.CharField(max_length=8)
    # time of meeting end
    endTime = models.CharField(max_length=8)

class Staff(User):
    ROLES = (
        ('T', 'TA'),
        ('I', 'Instructor'),
        ('A', 'Administrator'),
        ('S', 'Supervisor')
    )

    role = models.CharField(max_length=13, choices=ROLES)
    sections = models.ManyToManyField(Section) # For TA's
    courses = models.ManyToManyField(Course) # For instructors
    phonenum = models.CharField(max_length=10)
    address = models.CharField(max_length=30)