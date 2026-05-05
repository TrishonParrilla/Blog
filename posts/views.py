from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post
from django.contrib.auth.models import User 
from django.urls import reverse_lazy 

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
    template_name = "posts/new.html"
    model = Post
    # fields attrib is a list that lets us enable/disable inputs to render in html #using ajax to not rerender everything later(probably idk tbh)
    fields = ["title","subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        return super().form_valid(form)

class PostUpdateView(UpdateView): #Post request --> filled html form
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView): #Post request to delete
    template_name = "posts/delete.html"
    model = Post
    # success_url attrib redirects user if the user's req was successful
    success_url = reverse_lazy("post_list")

