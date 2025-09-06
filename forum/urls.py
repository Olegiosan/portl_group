from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('forum/', ForumLobby.as_view(), name  = "forum_lobby"),
]
