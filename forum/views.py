
from django.shortcuts import render
from django.views.generic import ListView

from forum.models import *


# Create your views here.

class ForumLobby(ListView):
    model = Post
    template_name = "forum/forum_lobby.html"
    context_object_name = "posts"



