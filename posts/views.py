from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post
class PostListView(ListView): #Get request that returns lists of posts from DB
    #template_name is the attribute to render the html
    template_name = "posts/list.html"
    #model attribute lets django know from which model(table) we want to retrieve data
    model = Post 
    #context object name allows us to change the variable name on how we call it inside of templates
    context_object_name = "posts"
# Create your views here.

class PostDetailView(DetailView): #Get Rquest -> single object/element
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView): #post request -> empty form(html)
    template_name = "posts/delete.html"
    model = Post
    # fields attrib is a list that lets us enable/disable inputs to render in html
    fields = ["title","subtitle", "body"]