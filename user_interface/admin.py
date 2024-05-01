from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Channel, ChannelOwner

# Register your models here.


@register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'picture_tag',
        'email',
        'first_name',
        'last_name',
    )
    readonly_fields = (
        'date_joined',
        'last_login',
        'picture_tag',
    )
    list_display_links = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('date_joined', 'last_login')


@register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'logo_tag',
        'description',
    )
    readonly_fields = (
        'created_date',
        'updated_date',
        'logo_tag',
        'description',
    )
    list_display_links = ('id', 'name')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('name', 'description')


@register(ChannelOwner)
class ChannelOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_info', 'channel_name')
    list_display_links = ('id',)
    list_filter = ('created_date', 'updated_date')

    @admin.display(ordering='id', description='Owner ID')
    def user_info(self, obj):
        return f"{obj.user.id}. {obj.user.username}"

    @admin.display(ordering='id', description='Channel Name')
    def channel_name(self, obj):
        return obj.channel.name
