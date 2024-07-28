from django.urls import path

from video.views import VideosListView

urlpatterns = [
    path('video_list', VideosListView.as_view(), name='video')
]