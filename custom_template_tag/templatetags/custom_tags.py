from django import template
register = template.Library()
from ..models import *

@register.simple_tag
def total_stu():
    return Student.objects.count()


# @register.filter(name='stud_name')
# def stud_name(name,school):
#     student = Student.objects.filter(name=name,school=school)
#     return student

# @register.filter(name='stud_name')
# def stud_name(arg_string):
#     args = arg_string.split(':')
#     name = args[0]
#     school = args[1]
#     fees = args[2]
#     student = Student.objects.filter(name=name, school=school, fees=fees)
#     return student



@register.inclusion_tag('custom_template_tag:indexs.html')          #not working
def student():
    products = Student.objects.all()
    return {'products': products}