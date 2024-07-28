from django.shortcuts import render
from django.views.generic import ListView

from video.models import Video


# Create your views here.


class VideosListView(ListView):
    template_name = 'video/video_list.html'
    model = Video
    context_object_name = 'videos'