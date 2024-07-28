from django.urls import path

from pictures.views import PicturesListView

urlpatterns = [
    path('pictures_list', PicturesListView.as_view(), name='picture')
]