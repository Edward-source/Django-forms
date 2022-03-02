from signal import raise_signal
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import *

# Create your views here.
class Post(View):

    def get(self, request, *args, **kwargs):

        form = postForm()
         
        return render(request, "blog/blog.html", {'FORM': form})

    def post(self, request, *args, **kwargs):
        
        try:

            form = postForm(request.POST)

        except:
            return 

        if form.is_valid(raise_signal):
            form.save()
            return HttpResponse("\success\\")