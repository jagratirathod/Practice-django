from django.contrib import admin
from . models import *


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','school','fees']
admin.site.register(Student,StudentAdmin)
