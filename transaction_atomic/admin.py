from django.contrib import admin
from . models import *



# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display=['id','user','amount']
admin.site.register(Payment,PaymentAdmin)
