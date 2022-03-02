
from django.contrib import admin
from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('blog_post/',blog_views.Post.as_view() , name = "blog-post")
]
