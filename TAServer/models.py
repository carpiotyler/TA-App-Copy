# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2
from django.db import models


# Placeholder model
class User(models.Model):
    @staticmethod
    def empty_user():
        u = User(username="", password="", role="")
        u.id = -1
        return u

    username = models.CharField(max_length = 20)
    password = models.CharField(max_length= 20)
    role = models.CharField(max_length=10, default="")


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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # room Number
    room = models.IntegerField(default=-1)
    # instructor or ta
    instructor = models.ForeignKey(User, default=User.empty_user(), on_delete= models.DO_NOTHING)
    # days of week meeting
    days = models.CharField(max_length=5, default="",choices=DAYS)
    # time of meeting ("05:45 AM" or "5:45 PM")
    startTime = models.CharField(max_length=8, default="")
    # time of meeting end
    endTime = models.CharField(max_length=8, default="")
