from django.db import models
from django.utils.html import mark_safe

from base_model.base_model import BaseModel
from user_interface.models import Channel

# Create your models here.


class Episode(BaseModel):
    title = models.TextField(verbose_name="Episode Title")
    audio_file = models.FileField(upload_to="audios/", verbose_name="Audio Content")
    image = models.ImageField(
        upload_to="content_images/",
        verbose_name="Image Content",
        blank=True,
        null=True,
    )

    def image_tag(self):
        if self.image:
            return mark_safe(
                '<img src="/media/{}" width=128px/>'.format(self.image)
            )
        else:
            return "No Image Found!"

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"
        ordering = ('created_date',)

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


class EpisodeMentions(BaseModel):
    episode = models.ForeignKey(
        Episode,
        on_delete=models.CASCADE,
        verbose_name="Episode",
        related_name="mentions",
    )
    channel = models.ManyToManyField(
        Channel,
        verbose_name="Channel Mentioned",
        related_name="mentions",
    )

    class Meta:
        verbose_name = "Episode Mentions"
        verbose_name_plural = "Episodes Mentions"
        ordering = ("created_date",)

    def __str__(self) -> str:
        channels = list(self.channel.all().values_list('name', flat=True))
        return f"{self.episode.title} - {', '.join(str(channel) for channel in channels)}"
