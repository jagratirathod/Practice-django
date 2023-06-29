from django.contrib import admin
from . models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','content','created_at','updated_at','author']
admin.site.register(Post,PostAdmin)

