from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
from .models import Menu


class MenuListView(ListView):
    """
    food menu as a list of items from the database
    """
    model = Menu
    template = 'menu/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
