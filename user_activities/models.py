from base_model.base_model import BaseModel, BaseModelWithUser
from content.models import Episode
from user_interface.models import Channel

from django.db import models

# Create your models here.


class EpisodeLikes(BaseModelWithUser):
    episode = models.ForeignKey(
        Episode,
        related_name="likes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Episode Like"
        verbose_name_plural = "Episode Likes"
        ordering = ("created_date",)

    def __str__(self):
        return self.user.username + f", liked this episode: {self.episode.title}"


class EpisodeDislikes(BaseModelWithUser):
    episode = models.ForeignKey(
        Episode,
        related_name="dislikes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Episode Dislike"
        verbose_name_plural = "Episode Dislikes"
        ordering = ("created_date",)

    def __str__(self):
        return self.user.username + f", disliked this episode: {self.episode.title}"


class SubscribedChannel(BaseModelWithUser):
    channel = models.ForeignKey(
        Channel,
        related_name="subscribed",
        verbose_name="Subscribed Channel",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Subscribed Channel"
        verbose_name_plural = "Subscribed Channels"
        ordering = ("created_date",)

    def __str__(self):
        return self.user.username + self.channel.name


class Comments(BaseModelWithUser):
    context = models.TextField(max_length=512, verbose_name="Context")
    episode = models.ForeignKey(
        Episode,
        related_name="comments",
        verbose_name="Episode",
        on_delete=models.CASCADE,
    )


class Playlist(BaseModelWithUser):
    name = models.CharField(max_length=255, verbose_name="Playlist Name")

    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"
        ordering = ("name",)

    def __str__(self):
        return self.name


class PlaylistEpisode(BaseModel):
    episode = models.ForeignKey(
        Episode,
        related_name="playlist_episode",
        verbose_name="Episode",
        on_delete=models.CASCADE,
    )
    playlist = models.ForeignKey(
        Playlist,
        related_name="playlist_episode",
        verbose_name="Playlist",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Playlist Episode"
        verbose_name_plural = "Playlist Episodes"
        ordering = ("created_date",)

    def __str__(self):
        return self.episode.title + self.playlist.name
