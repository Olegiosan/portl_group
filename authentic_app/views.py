from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


from authentic_app.models import CustomUser


# Create your views here.
class LoginUserView(LoginView):
    template_name = "auth/login_user.html"
    authentication_form = AuthenticationForm

