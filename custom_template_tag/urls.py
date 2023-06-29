from django.urls import path
from. import views

app_name = "custom_template_tag"

urlpatterns = [
    path('',views.index,name="index")
]