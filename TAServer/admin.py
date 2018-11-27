from django.contrib import admin
from .models import Course, User, Section

admin.site.register(Course)
admin.site.register(Section)
# Register your models here.