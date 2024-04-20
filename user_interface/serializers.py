from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Channel, ChannelOwner, ChannelEpisode
from content.serializers import EpisodeSerializer

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password',
            'groups',
            'user_permissions',
            'is_active',
            'is_staff',
            'is_superuser',
        )


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        exclude = ("is_allowed",)


class ChannelOwnerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    channel = ChannelSerializer(read_only=True)

    class Meta:
        model = ChannelOwner
        fields = (
            "id",
            "user",
            "channel",
            "description",
            "created_date",
            "updated_date",
        )


class ChannelEpisodeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    episode = EpisodeSerializer(read_only=True)

    class Meta:
        model = ChannelEpisode
        fields = (
            "id",
            "user",
            "episode",
            "description",
            "created_date",
            "updated_date",
        )
