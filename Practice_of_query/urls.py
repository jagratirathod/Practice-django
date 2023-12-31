"""Practice_of_query URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include('app1.urls')),
    path('tag/',include('custom_template_tag.urls')),
    path('save_method/',include('save_method.urls')),
    path('signal_app/',include('signal_app.urls')),
    path('transaction_atomic/',include('transaction_atomic.urls')),
    path('customize_admin/',include('customize_admin.urls')),
    path('model_inheritance/',include('model_inheritance.urls')),
    path('property_decorator/',include('property_decorator.urls')),

]

