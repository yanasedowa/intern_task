from django.urls import path
from . import views

urlpatterns = [
    path('video_maker/', views.video_maker, name='video_maker'),
]
