from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *


# Create your views here.
class PortfolioLobby(ListView):
    model = Portfolio
    template_name = "portfolio/portf_lobby.html"
    context_object_name = "portfolios"
    paginate_by = 2

class PortfolioDetails(DetailView):
    model = Portfolio
    template_name = "portfolio/portf_details.html"
    context_object_name = "portfolio"

class LikeOrDislikePortfolios(View):
    def post(self, request, *args, **kwargs):
        reaction = kwargs.get("reaction")
        pk = kwargs.get("pk")
        current_port = Portfolio.objects.get(pk=pk)
        likes = current_port.likes.filter(pk=request.user.pk).exists()
        dislikes = current_port.dislikes.filter(pk=request.user.pk).exists()
        if reaction == 'like':
            if not likes:
                current_port.likes.add(request.user)
            else:
                current_port.likes.remove(request.user)
        elif reaction == 'dislike':
            if not dislikes:
                current_port.dislikes.add(request.user)
            else:
                current_port.dislikes.remove(request.user)
        return redirect("portf_lobby")