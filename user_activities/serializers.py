from rest_framework import serializers

from .models import (
    EpisodeLikes,
    EpisodeDislikes,
    Comments,
    Playlist,
    PlaylistEpisode,
    SubscribedChannel,
)

from user_interface.serializers import CustomUserSerializer, ChannelSerializer
from content.serializers import EpisodeSerializer


class EpisodeLikesSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    episode = EpisodeSerializer(read_only=True)

    class Meta:
        model = EpisodeLikes
        fields = (
            'id',
            'user',
            'episode',
            'created_date',
            'updated_date',
        )


class EpisodeDislikesSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    episode = EpisodeSerializer(read_only=True)

    class Meta:
        model = EpisodeDislikes
        fields = (
            "id",
            "user",
            "episode",
            "created_date",
            "updated_date",
        )


class CommentsSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    episode = EpisodeSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = (
            "id",
            "user",
            "episode",
            "context",
            "created_date",
            "updated_date",
        )


class PlaylistSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Playlist
        fields = (
            "id",
            "user",
            "name",
            "description",
            "created_date",
            "updated_date",
        )


class PlaylistEpisodeSerializer(serializers.ModelSerializer):
    playlist = PlaylistSerializer(read_only=True)
    episode = EpisodeSerializer(read_only=True)

    class Meta:
        model = PlaylistEpisode
        fields = (
            "id",
            "playlist",
            "episode",
            "created_date",
            "updated_date",
        )


class SubscribedChannelSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    channel = ChannelSerializer(read_only=True)

    class Meta:
        model = SubscribedChannel
        fields = (
            "id",
            "user",
            "channel",
            "created_date",
            "updated_date",
        )
