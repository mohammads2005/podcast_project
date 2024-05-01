from django.contrib import admin
from django.contrib.admin import register

from .models import (
    EpisodeLikes,
    EpisodeDislikes,
    SubscribedChannel,
    Comments,
    Playlist,
    PlaylistEpisode,
)


# Register your models here.

class BaseAdminModel(admin.ModelAdmin):
    list_display_links = ('id',)

    @admin.display(ordering='id', description='User Info')
    def user_info(self, obj):
        return f"{obj.user.id}. {obj.user.username}"

    @admin.display(ordering='created_date', description='Episode Title')
    def episode_title(self, obj):
        return obj.episode.title


@register(*(EpisodeLikes, EpisodeDislikes, Comments))
class LikeDislikeAdmin(BaseAdminModel):
    list_display = ('id', 'user_info', 'episode_title')
    list_filter = (
        'episode__title',
        'user__username',
        'created_date',
        'updated_date',
    )
    search_fields = ('episode__title', 'user__username')
    autocomplete_fields = ('episode', 'user')


@register(SubscribedChannel)
class SubscribedChannelAdmin(BaseAdminModel):
    list_display = ('id', 'user_info', 'channel_name')
    list_filter = (
        'user__username',
        'channel__name',
        'created_date',
        'updated_date',
    )
    search_fields = ('user__username', 'channel__name')
    autocomplete_fields = ('user', 'channel')

    @admin.display(ordering='id', description='Channel Name')
    def channel_name(self, obj):
        return obj.channel.name


@register(Playlist)
class PlaylistAdmin(BaseAdminModel):
    list_display = ('id', 'user_info', 'name')
    list_filter = (
        'user__username',
        'name',
        'created_date',
        'updated_date',
    )
    search_fields = ('user__username', 'name')
    autocomplete_fields = ('user',)


@register(PlaylistEpisode)
class PlaylistEpisodeAdmin(BaseAdminModel):
    list_display = ('id', 'user_info', 'episode_title', 'playlist_name')
    list_filter = (
        'episode__title',
        'playlist__name',
        'created_date',
        'updated_date',
    )
    search_fields = ('episode__title', 'playlist__name')
    autocomplete_fields = ('episode', 'playlist')

    @admin.display(ordering='id', description='Playlist Name')
    def playlist_name(self, obj):
        return obj.playlist.name

    @admin.display(ordering='id', description='User Info')
    def user_info(self, obj):
        return f"{obj.playlist.user.id}. {obj.playlist.user.username}"
