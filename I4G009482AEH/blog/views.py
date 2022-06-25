# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views import generic
# from blog.models import Post


# # Create your views here.


# class PostListView(generic.Listview):
#   model=  Post

# class PostCreateView(generic.Createview):
#   model= Post
#   fields="__all__"
# success_url=reverse_lazy("blog:all")

# class PostDetailView(generic.Detailview):
#   model= Post

# class PostUpdateView(generic.Updateview):
#    model= Post
#    fields="__all__"
#    success_url=reverse_lazy("blog:all")

# class PostDeleteView(generic.Deleteview):
#   model= Post
#   fields="__all__"
#   success_url=reverse_lazy("blog:all")
  

from django.shortcuts import render
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from blog.models import Post
from .models import *

# Create your views here.


class PostListView(ListView):
    model = Post
template_name = "blog/post_list.html"


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
template_name = "blog/post_form.html"

class PostDetailView(DetailView):
    model = Post
template_name = "blog/post_detail.html"

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
template_name = "blog/post_form.html"

class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
template_name = "blog/post_confirm_delete.html"