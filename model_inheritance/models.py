from django.db import models

# Create your models here.


#  Abstract base class -

class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    
    class Meta:
        abstract = True


class Student(CommonInfo):
    fees = models.IntegerField()
    date = None

    # class Meta:
    #     verbose_name = "Just check"
    #     verbose_name_plural = "Custom Student Name"


class Teacher(CommonInfo):
    salary = models.IntegerField()


class Contractor(CommonInfo):
    date =  models.DateField()
    payment = models.IntegerField()



# multi-table inheritance - 

class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.cname


class MyStudent(ExamCenter):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    def __str__(self):
        return self.name
    

# Proxy model - 

class Center(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length = 70)


class MyCenter(Center):
    class Meta:
        proxy = True
        ordering = ['id']






