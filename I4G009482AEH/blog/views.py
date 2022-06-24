from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from models import Post

# Create your views here.


class PostListView(generic.Listview):
  model=  Post

class PostCreateView(generic.Createview):
  model= Post
  fields="__all__"
success_url=reverse_lazy("blog:all")

class PostDetailView(generic.Detailview):
  model= Post

class PostUpdateView(generic.Updateview):
   model= Post
   fields="__all__"
   success_url=reverse_lazy("blog:all")

class PostDeleteView(generic.Deleteview):
  model= Post
  fields="__all__"
  success_url=reverse_lazy("blog:all")
  
