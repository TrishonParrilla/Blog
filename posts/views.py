from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post, Status
from django.contrib.auth.models import User 
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)    

class PostListView(ListView): #Get request that returns lists of posts from DB
    #template_name is the attribute to render the html
    template_name = "posts/list.html"
    #model attribute lets django know from which model(table) we want to retrieve data
    #model = Post 
    published_status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=published_status).order_by("created_on") #can use .reverse() to reverse order of posts
    #context object name allows us to change the variable name on how we call it inside of templates
    context_object_name = "posts"
# Create your views here.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "published"
        #print(context)
        # context["extra"] = "This is some extra context data" <-- we can add extra context and add elements with <p>{{extra}}</p>
        return context



class PostDetailView(LoginRequiredMixin, DetailView): #Get Rquest -> single object/element
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

     #filtering posts by published status and reversing order of posts .reverse()

class PostCreateView(LoginRequiredMixin, CreateView): #post request -> empty form(html)
    template_name = "posts/new.html"
    model = Post
    # fields attrib is a list that lets us enable/disable inputs to render in html #using ajax to not rerender everything later(probably idk tbh)
    fields = ["title","subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView): #Post request --> filled html form
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    #test func checks to see if user is authenticated and if they are an author. if it is true it renders the form, if not it redirects to login page
    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False
        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #Post request to delete
    template_name = "posts/delete.html"
    model = Post
    # success_url attrib redirects user if the user's req was successful
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False

class PostArchivedListView(ListView):
    template_name = "posts/list.html"
    archived_status = Status.objects.get(name="archived")
    queryset = Post.objects.filter(status=archived_status)
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "archived"
        return context

class PostDraftListView(ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        draft_status = Status.objects.get(name="draft")
        return Post.objects.filter(status=draft_status)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "draft"
        return context
    