
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import View
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

class LikeOrDislikePosts(View):
    def post(self, request, *args, **kwargs):
        reaction = kwargs.get("reaction")
        pk = kwargs.get("pk")
        current_post = Post.objects.get(pk=pk)
        likes = current_post.likes.filter(pk=request.user.pk).exists()
        dislikes = current_post.dislikes.filter(pk=request.user.pk).exists()
        if reaction == 'like':
            if not likes:
                current_post.likes.add(request.user)
            else:
                current_post.likes.remove(request.user)
        elif reaction == 'dislike':
            if not dislikes:
                current_post.dislikes.add(request.user)
            else:
                current_post.dislikes.remove(request.user)
        return redirect("forum_lobby")