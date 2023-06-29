from django.urls import path
from. import views

app_name = "signal_app"

urlpatterns = [
    path('',views.PostView.as_view(),name="Posts")
]
