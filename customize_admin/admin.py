from django.contrib import admin
from .models import Widget 
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import get_object_or_404
from django.urls import reverse


# Register your models here.


class WidgetAdmin(admin.ModelAdmin):
    list_display = ['id','name','font_size']
admin.site.register(Widget, WidgetAdmin)


# class WidgetAdmin(admin.ModelAdmin):
#     list_display = ['id','name','font_size']
#     actions = ['get_name']

#     def get_name(self,request,queryset):
#         queryset.update(name="rohan")
# admin.site.register(Widget,WidgetAdmin)


# class WidgetAdmin(admin.ModelAdmin):
#     list_display = ['id','name','font_size']
#     actions = ['get_name']

#     def get_name(self,request,queryset):
#         wids=Widget.objects.filter(id=queryset.first().id)
#         context = {'wids': wids}
#         return render(request, 'admin/wid_list.html', context)
# admin.site.register(Widget,WidgetAdmin)


# class WidgetAdmin(admin.ModelAdmin):
#     list_display = ['id','name','font_size_html_display'] 
#     change_list_template = 'admin/widgets_list.html'
    
#     def get_urls(self):
#         urls = super().get_urls()   
#         custom_urls = [
#             path('fontsize/<int:size>/',self.change_font_size)
#         ]
#         return custom_urls + urls  
    
#     def change_font_size(self,request, size):
#         self.model.objects.update(font_size=size) 
#         self.message_user(request,'font size set Successfully')
#         return HttpResponseRedirect("../..")

#     def font_size_html_display(self,obj):
#         display_size=obj.font_size if obj.font_size>=30 else None
#         return format_html(
#             f'<span style="font-size:{display_size}px;">{obj.font_size}</span>'
#             )
# admin.site.register(Widget,WidgetAdmin)



