from django.db import models

# Create your models here.


class Widget(models.Model):
    name = models.CharField(max_length=140)
    font_size=models.IntegerField()
    
    def __str__(self):
        return self.name
