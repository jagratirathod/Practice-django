from django.urls import path
from. import views

app_name = "save_method"

urlpatterns = [
    path('',views.PostView.as_view(),name="Posts")
]
