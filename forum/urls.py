from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('forum/', ForumLobby.as_view(), name="forum_lobby"),
    path('forum/<int:pk>', PostDetails.as_view(), name = "post_details"),
    path('forum/reaction/<str:reaction>/<int:pk>', LikeOrDislikePosts.as_view(), name = "like_or_dislike")
]
