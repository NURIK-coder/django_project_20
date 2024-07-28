from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from books.models import FavouriteItem
from users.forms import RegisterForm, LoginForm


# Create your views here.

class RegisterUserView(CreateView):
    template_name = 'auth_register/register.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('main')


class LoginUserView(LoginView):
    template_name = 'auth_register/login.html'
    success_url = reverse_lazy('main')


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favourite_books = FavouriteItem.objects.filter(user=self.request.user,
                                                       content_type='books.book').order_by('-id')[:3]
        favourite_music = FavouriteItem.objects.filter(user=self.request.user,
                                                       content_type='music.music').order_by('-id')[:3]

        context['favourite_books'] = favourite_books
        context['favourite_music'] = favourite_music

        return context


class LogoutUserView(LogoutView):
    success_url = reverse_lazy('main')
