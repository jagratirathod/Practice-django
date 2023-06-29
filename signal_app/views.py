from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . models import *
from . forms import *
from datetime import timedelta
from django.utils import timezone


# Create your views here.

class PostView(CreateView):
    model = Post
    form_class = Postform
    template_name = "posthere.html"
    success_url = reverse_lazy("signal_app:Posts")

    def form_valid(self,form):
            form.instance.created_at=timezone.now()+timedelta(days=4)
            form.instance.author = self.request.user
            return super().form_valid(form)