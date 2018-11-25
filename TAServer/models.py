# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.contrib.auth.models import User
from django.db import models


class TAGroup(models.Group):
    permissions = (("can_edit_self", "Can edit users"),
                   ("can_view_users", "Can view users"))


class InsGroup(models.Group):
    permissions = (("can_view_courses", "Can view courses"),

                   ("can_edit_self", "Can edit users"),
                   ("can_view_users", "Can view users"),
                   ("can_view_private", "Can view private user data"),

                   ("can_assign_ta", "Can assign TA's"),

                   ("can_email_tas", "Can send emails"))


class AdminGroup(models.Group):
    permissions = (("can_create_course", "Can create courses"),
                   ("can_edit_courses", "Can edit courses"),
                   ("can_delete_courses", "Can delete courses"),
                   ("can_view_courses", "Can view courses"),

                   ("can_create_sections", "Can create sections"),
                   ("can_edit_sections", "Can edit sections"),
                   ("can_delete_sections", "Can delete sections"),
                   ("can_view_sections", "Can view sections"),

                   ("can_create_users", "Can create users"),
                   ("can_edit_users", "Can edit users"),
                   ("can_edit_self", "Can edit users"),
                   ("can_delete_users", "Can delete users"),
                   ("can_view_users", "Can view users"),
                   ("can_view_private", "Can view private user data"),

                   ("can_email_all", "Can send emails to all users"))


class SupGroup(models.Group):
    permissions = (("can_create_course", "Can create courses"),
                   ("can_edit_courses", "Can edit courses"),
                   ("can_delete_courses", "Can delete courses"),
                   ("can_view_courses", "Can view courses"),

                   ("can_create_sections", "Can create sections"),
                   ("can_edit_sections", "Can edit sections"),
                   ("can_delete_sections", "Can delete sections"),
                   ("can_view_sections", "Can view sections"),

                   ("can_create_users", "Can create users"),
                   ("can_edit_users", "Can edit users"),
                   ("can_edit_self", "Can edit users"),
                   ("can_delete_users", "Can delete users"),
                   ("can_view_users", "Can view users"),
                   ("can_view_private", "Can view private user data"),

                   ("can_assign_ta", "Can assign TA's"),
                   ("can_assign_ins", "Can assign instructors"),

                   ("can_email_all", "Can send emails to all users"))


class Staff(User):
    ROLES = (
        ('T', 'TA'),
        ('I', 'Instructor'),
        ('A', 'Administrator'),
        ('S', 'Supervisor')
    )

    role = models.CharField(max_length=13, choices=ROLES)
    sections = models.ManyToManyField(Section, default="default")  # For TA's
    courses = models.ManyToManyField(Course, default="default")  # For instructors
    phonenum = models.CharField(max_length=10)
    address = models.CharField(max_length=30)

    def default(self):
        pass  # Do something
