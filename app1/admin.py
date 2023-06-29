from django.contrib import admin
from . models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','name','tagline']
admin.site.register(Blog,BlogAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','name' , 'email']
admin.site.register(Author,AuthorAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display=['id','blog','headline','body_text','pub_date','mod_date',
    'number_of_comments','number_of_pingbacks','rating','get_authors']
admin.site.register(Entry,EntryAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display=['id','name','shirt_size','birth_date']
admin.site.register(Person,PersonAdmin)
