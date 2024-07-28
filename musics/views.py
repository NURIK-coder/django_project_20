from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from musics.forms import MusicCreateForm
from musics.forms import MusicUpdateForm
from musics.models import Music


# Create your views here.

class MusicsListView(ListView):
    template_name = 'musics/musics_list.html'
    model = Music
    context_object_name = 'musics'


class MusicCreateView(CreateView):
    model = Music
    form_class = MusicCreateForm
    template_name = 'musics/create.html'
    success_url = reverse_lazy('music_list')

    def test_func(self):
        return self.request.user.is_superuser


class MusicUpdateView(UpdateView):
    model = Music
    form_class = MusicUpdateForm
    template_name = 'musics/update.html'
    success_url = reverse_lazy('music_list')

    def test_func(self):
        return self.request.user.is_superuser


class MusicDeleteView(DeleteView):
    model = Music
    success_url = reverse_lazy('music_list')
    template_name = 'musics/delete.html'

    def test_func(self):
        return self.request.user.is_superuser


class MusicDetailView(DetailView):
    model = Music
    context_object_name = 'music'
