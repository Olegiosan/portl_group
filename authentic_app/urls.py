from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginUserView.as_view(), name  = "user_login"),
]
