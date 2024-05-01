from django.urls import path, include
from rest_framework import routers

from .views import (
    EpisodeModelView,
    NewEpisodeFormView,
    EpisodeMentionsFormView,
    ChannelEpisodesView,
    EpisodeDownloadView,
    AudioPlayerView,
)

episode_router = routers.DefaultRouter()
episode_router.register('', EpisodeModelView)

urlpatterns = [
    path('episodes/', include(episode_router.urls)),
    path('new_podcast/mention/<int:pk>', EpisodeMentionsFormView.as_view(), name='mention'),
    path('new_podcast/', NewEpisodeFormView.as_view(), name='upload_new_podcast'),
    path('channel/<int:pk>/episodes', ChannelEpisodesView.as_view(), name='channel_episodes'),
    path('episode/<int:pk>/download', EpisodeDownloadView.as_view(), name='download_episode'),
    path('episode/<int:pk>/play', AudioPlayerView.as_view(), name='play_audio'),
]
