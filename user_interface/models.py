from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from base_model.base_model import BaseModel

# Create your models here.


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", verbose_name="Profile Pictures"
    )
    bio = models.TextField(verbose_name="Bio")
    social_link = models.URLField(verbose_name="Social Link")

    class Meta:
        db_table = "custom_user"
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        ordering = ("username",)


class Channel(BaseModel):
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Channel's Name"
    )
    logo = models.ImageField(
        upload_to="logos/", verbose_name="Channel's Logo"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self) -> str:
        return self.name


class ChannelOwner(BaseModel):
    channel = models.ForeignKey(
        Channel,
        related_name="channel_owner",
        verbose_name="Channel",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="channel_owner",
        verbose_name="User",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Channel & Owner"
        verbose_name_plural = "Channels & Owners"

    def __str__(self) -> str:
        return self.channel.name
