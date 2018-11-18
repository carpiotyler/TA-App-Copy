# This file is copied straight from Rock's provided code under "Skeleton code for Django" in sprint 2

from django.db import models


class User(models.Model):
    username = models.CharField(max_length = 40)
    password = models.CharField(max_length = 40)
    role = models.CharField(max_length = 40)

    def __str__(self):
        pass
