from django.urls import path

from base.views import BaseView

urlpatterns = [
    path('main_page/', BaseView.as_view(), name='main'),
]