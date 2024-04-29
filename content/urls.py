from django.urls import path, include
from rest_framework import routers

from .views import EpisodeModelView, NewEpisodeFormView

episode_router = routers.DefaultRouter()
episode_router.register('', EpisodeModelView)

urlpatterns = [
    path('episodes/', include(episode_router.urls)),
    path('new_podcast/', NewEpisodeFormView.as_view(), name='upload_new_podcast'),
]
