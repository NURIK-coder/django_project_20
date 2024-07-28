from django.shortcuts import render
from django.views.generic import ListView

from pictures.models import Picture


# Create your views here.


class PicturesListView(ListView):
    template_name = 'pictures/pictures_list.html'
    model = Picture
    context_object_name = 'pictures'