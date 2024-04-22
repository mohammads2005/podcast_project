from django.db import models
# from django.conf import settings

from base_model.base_model import BaseModel
from user_interface.models import Channel


# Create your models here.


class Episode(BaseModel):
    title = models.TextField(verbose_name="Episode Title")
    audio_file = models.FileField(upload_to="audios/", verbose_name="Audio Content")
    channel_mentions = models.ManyToManyField(
        Channel, related_name="episode", verbose_name="Channel Mentions", blank=True,
    )

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"
        ordering = ['created_date']

    def __str__(self):
        return self.title


class EpisodeChannel(BaseModel):
    episode = models.ForeignKey(
        Episode,
        on_delete=models.CASCADE,
        related_name="channel_episode",
        verbose_name="Episode",
    )
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        related_name="channel_episode",
        verbose_name="Channel",
    )

    class Meta:
        verbose_name = "Channel's Episode"
        verbose_name_plural = "Channel's Episodes"
        ordering = ("created_date",)

    def __str__(self) -> str:
        return self.channel.name + self.episode.title
