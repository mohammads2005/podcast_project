from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe

from base_model.base_model import BaseModel

# Create your models here.


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        verbose_name="Profile Pictures",
        blank=True,
        null=True,
    )
    bio = models.TextField(max_length=255, verbose_name="Bio", blank=True)
    social_link = models.URLField(verbose_name="Social Link", blank=True)

    def picture_tag(self):
        if self.profile_picture:
            return mark_safe(
                '<img src="/media/{}" width=128px/>'.format(self.profile_picture)
            )
        else:
            return "No Picture Found!"

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

    def logo_tag(self):
        if self.logo:
            return mark_safe(
                '<img src="/media/{}" width=128px/>'.format(self.logo)
            )
        else:
            return "No Logo Found!"

    class Meta:
        ordering = ("name",)
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self) -> str:
        return self.name


class ChannelOwnerManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None


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
    objects = ChannelOwnerManager()

    class Meta:
        verbose_name = "Channel & Owner"
        verbose_name_plural = "Channels & Owners"

    def __str__(self) -> str:
        return self.channel.name
