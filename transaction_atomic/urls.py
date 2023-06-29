from django.urls import path
from. import views

app_name = "transaction_atomic"

urlpatterns = [
    path('',views.homeView,name="home")
]
