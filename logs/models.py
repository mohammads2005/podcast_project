from django.db import models

from base_model.base_model import BaseModelWithUser
from user_interface.models import Channel
from content.models import Episode

# Create your models here.


class ChannelVisit(BaseModelWithUser):
    channel = models.ForeignKey(
        Channel,
        related_name="channel_visit",
        verbose_name="Channel",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Channel Visit'
        verbose_name_plural = 'Channel Visits'
        ordering = ("created_date",)

    def __str__(self):
        return f"Channel Visit: {self.channel.name} - {self.created_date.strftime("%d.%m.%Y %H:%M")}"


class EpisodeListened(BaseModelWithUser):
    episode = models.ForeignKey(
        Episode,
        related_name="episode_visit",
        verbose_name="Episode",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Episode Listened'
        verbose_name_plural = 'Episodes Listened'
        ordering = ("created_date",)

    def __str__(self):
        return f"Episode Listened: {self.episode.title} - {self.created_date.strftime("%d.%m.%Y %H:%M")}"


class EpisodeDownloads(BaseModelWithUser):
    episode = models.ForeignKey(
        Episode,
        related_name="episode_downloads",
        verbose_name="Episode",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Episode Download'
        verbose_name_plural = 'Episode Downloads'
        ordering = ("created_date",)

    def __str__(self):
        return f"Episode Downloaded: {self.episode.title} - {self.created_date.strftime("%d.%m.%Y %H:%M")}"
