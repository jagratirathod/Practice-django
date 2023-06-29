from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=60)
    school=models.CharField(max_length=60)
    fees = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    



# class Person(models.Model):
#     SHIRT_SIZES = [
#         ("S", "Small"),
#         ("M", "Medium"),
#         ("L", "Large"),
#     ]
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
#     birth_date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return self.name

