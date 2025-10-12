from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('portfolio/', PortfolioLobby.as_view(), name="portf_lobby"),
    path('portfolio_details/<int:pk>', PortfolioDetails.as_view(), name="portf_details"),
    path('portfolio/reaction/<str:reaction>/<int:pk>', LikeOrDislikePortfolios.as_view(), name="like_or_dislikes"),
]
