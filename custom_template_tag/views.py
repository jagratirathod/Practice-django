from django.shortcuts import render
from django.http import HttpResponse
from . models import  *
# Create your views here.


def index(request):
    studs = Student.objects.all()
    return render(request,"indexs.html",{"studs":studs})