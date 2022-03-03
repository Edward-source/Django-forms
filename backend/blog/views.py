from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import *

# Create your views here.
class Post(View):
    
    """
    Inherit parent Views class for all views.
    Intentionally simple parent class for all get and post views.
    """

    def get(self, request, *args, **kwargs):

        form = postForm()
         
        return render(request, "blog/blog.html", {'FORM': form})

    def post(self, request, *args, **kwargs):

        http_error= "<h1>Error !</h1>"
        http_success="<h1> Posted !</h1>"

        try:

            form = postForm(request.POST)
            print(request.POST)

        except:
            return HttpResponse(http_error)

        if form.is_valid():
            print("Saving ...")
            form.save()
        return HttpResponse(http_success)
        