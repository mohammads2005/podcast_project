from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Channel, ChannelOwner
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

    def __init__(self, *args, **kwargs):
        exclude = kwargs.pop('exclude', None)
        super(CustomUserSerializer, self).__init__(*args, **kwargs)

        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name)


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
