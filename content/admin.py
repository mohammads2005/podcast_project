from django.contrib import admin
from django.contrib.admin import register

from .models import Episode, ChannelEpisode

# Register your models here.


@register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'audio_file', 'created_date')
    list_filter = ('created_date', 'updated_date', 'channel_mentions')
    list_display_links = ('id', 'title')
