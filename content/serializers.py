from rest_framework import serializers

from .models import Episode, EpisodeChannel, EpisodeMentions


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        exclude = ("is_allowed",)


class EpisodeChannelSerializer(serializers.ModelSerializer):
    episode = EpisodeSerializer(read_only=True)

    class Meta:
        model = EpisodeChannel
        exclude = ("is_allowed", "channel", "description")
