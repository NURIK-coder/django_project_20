from django.urls import path

from musics.views import MusicsListView, MusicCreateView, MusicUpdateView, MusicDeleteView, MusicDetailView

urlpatterns = [
    path('music_list/', MusicsListView.as_view(), name='music'),
    path('music_create/<int:pk>', MusicCreateView.as_view(), name='book_create'),
    path('music_update/<int:pk>', MusicUpdateView.as_view(), name='music_update'),
    path('music_delete/<int:pk>', MusicDeleteView.as_view(), name='music_delete'),
    path('music_detail/<int:pk>', MusicDetailView.as_view(), name='music_delete'),
]