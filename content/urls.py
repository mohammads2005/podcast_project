from django.urls import path, include
from rest_framework import routers

from .views import upload_new_podcast, EpisodeModelView

episode_router = routers.DefaultRouter()
episode_router.register('', EpisodeModelView)

urlpatterns = [
    path('new_podcast/', upload_new_podcast, name='upload_new_podcast'),
    path('episodes/', include(episode_router.urls)),
]
