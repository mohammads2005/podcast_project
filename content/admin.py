from django.contrib import admin
from django.contrib.admin import register

from .models import Episode, EpisodeChannel, EpisodeMentions

# Register your models here.


@register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'image_tag',
        'description',
        'audio_file',
        'created_date',
    )
    list_display_links = ('id', 'title')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('title', 'description')


@register(EpisodeChannel)
class EpisodeChannelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_episode_title',
        'get_channel_name',
        'created_date',
    )
    list_display_links = ('id',)
    list_filter = ('created_date', 'updated_date')

    @admin.display(ordering='created_date', description='Title')
    def get_episode_title(self, obj):
        return obj.episode.title

    @admin.display(ordering='created_date', description='Channel Name')
    def get_channel_name(self, obj):
        return obj.channel.name


@register(EpisodeMentions)
class EpisodeMentionsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_episode_title', 'get_channel_name',
    )
    list_display_links = ('id',)
    list_filter = ('created_date', 'updated_date')

    @admin.display(ordering='created_date', description='Title')
    def get_episode_title(self, obj):
        return obj.episode.title

    @admin.display(ordering='created_date', description='Channel Name')
    def get_channel_name(self, obj):
        return obj.channel.name
