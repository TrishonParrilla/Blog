from django.shortcuts import render
from django.views.generic import (
    ListView
)

from .models import Post
class PostListView(ListView):
    #template_name is the attribute to render the html
    template_name = "posts/list.html"
    #model attribute lets django know from which model(table) we want to retrieve data
    model = Post 
    #context object name allows us to change the variable name on how we call it inside of templates
    context_object_name = "posts"
# Create your views here.
