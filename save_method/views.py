from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . models import *
from . forms import *

# Create your views here.

class PostView(CreateView):
    model = Post
    form_class = Postform
    template_name = "addpost.html"
    success_url = reverse_lazy("save_method:Posts")

    # def form_valid(self,form):
    #         form.instance.created_at=timezone.now()+timedelta(days=3)
    #         return super().form_valid(form)