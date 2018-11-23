# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2
from django.db import models


# Placeholder model
class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length= 20)
    role = models.CharField(max_length=10)

class Course(models.Model):
    cnum = models.CharField(max_length = 4)
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 200)
    dept = models.CharField(max_length = 10)

    def __str__(self):
        pass

    # returns all sections for course
    def sections (self):
        pass


class Section(models.Model):

    # section type
    SEC_TYPE = (
        'lab'
        'lecture'
    )
    # days to meet (M=Monday, T=Tuesday, W=Wednesday, H=Thursday, F=Friday)
    DAYS = (
        'M',
        'T',
        'W',
        'H',
        'F',
        'MW',
        'TH',
        'MWF',
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
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    # days of week meeting
    days = models.CharField(max_length=5, choices=DAYS)
    # time of meeting ("05:45 AM" or "5:45 PM")
    time = models.CharField(max_length=8)
