# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.db import models

# Create your models here.


class Section(models.Model):
    # only two types of users can possibly teach a section
    INS_TYPE = (
        'TA',
        'instructor',
    )
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
    roomNum = models.IntegerField()
    # instructor or ta
    instructor = models.CharField(max_length=10, choices=INS_TYPE)
    # days of week meeting
    days = models.CharField(max_length=5, choices=DAYS)
    # time of meeting ("05:45 AM" or "5:45 PM")
    time = models.CharField(max_length=8)