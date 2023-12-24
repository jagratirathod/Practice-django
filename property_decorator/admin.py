from django.contrib import admin
from . models import *


# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' , 'description']
admin.site.register(MyModel, MyModelAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' , 'position' ,'salary']
admin.site.register(Employee, EmployeeAdmin)



class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' , 'city']
admin.site.register(Department, DepartmentAdmin)

