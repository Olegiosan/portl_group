
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from forum.models import *


# Create your views here.

class ForumLobby(ListView):
    model = Post
    template_name = "forum/forum_lobby.html"
    context_object_name = "posts"
    paginate_by = 2

class PostDetails(DetailView):
    model = Post
    template_name = "forum/post_details.html"
    context_object_name = "post"
