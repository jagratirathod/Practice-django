from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
@receiver(post_save,sender=Post)
def send_notification(sender,instance,created,**kwargs):
    if created:
        print("--------------",sender)
        subject = 'New blog post published!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['shuyadav@bestpeers.com',]

        message = f'Hi{instance.author}, A new post title {instance.title} has been published on your blog'
        send_mail(subject,message,email_from,recipient_list)

    
