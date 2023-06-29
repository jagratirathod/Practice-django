from django.db import models
from django.utils import timezone
from datetime import timedelta

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.created_at = timezone.now()+timedelta(days=3)
        super().save(*args, **kwargs)
