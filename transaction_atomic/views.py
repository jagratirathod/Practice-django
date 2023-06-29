from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . models import *
from django.contrib import messages
from django.db import transaction

# Create your views here.


def homeView(request):
    if request.method=="POST":
        try:
            user_one = request.POST.get("user_one")
            user_two = request.POST.get("user_two")
            amount = request.POST.get("amount")

            with transaction.atomic():
                user1 = get_object_or_404(Payment, user = user_one)
                if user1.amount >= int(amount):
                    user1.amount -= int(amount)
                    user1.save()
                else:
                    messages.success(request,"Not enough balance!")
                    return HttpResponse(messages)
                
                user2 = get_object_or_404(Payment, user = user_two)
                user2.amount+= int(amount)
                user2.save()
                messages.success(request,'Your amount is transfered')

        except Exception as e:
            print(e)
            messages.success(request,"Something went wrong")

    return render(request,"home.html")

def cmp(a,b):
    if a:
        return a>b
    else :
        return False