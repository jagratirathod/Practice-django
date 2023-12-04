from django.contrib import admin
from . models import *

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','fees','name','age']
admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','salary','name','age','date']
admin.site.register(Teacher, TeacherAdmin)


# class ContractorAdmin(admin.ModelAdmin):
#     list_display = ['id','payment','name','age','date']
# admin.site.register(Contractor, ContractorAdmin)


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id','payment','name','age','date']
    
# --------------------------------------------------------------------------------------------------

class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname' , 'city']
admin.site.register(ExamCenter, ExamCenterAdmin)


class MyStudentAdmin(admin.ModelAdmin):
    list_display = ['id','name' , 'roll' , 'cname' , 'city']
admin.site.register(MyStudent, MyStudentAdmin)


# ---------------------------------------------------------------------------------------------------


class CenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']
admin.site.register(Center, CenterAdmin)


class MyCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']
admin.site.register(MyCenter, MyCenterAdmin)







