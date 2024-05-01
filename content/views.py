import os
# import puydub.utils import mediainfo

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import redirect, HttpResponse, get_object_or_404, render
from django.views.generic.edit import FormView
from django.core.exceptions import ValidationError

from .forms import EpisodeForm, EpisodeMentionsForm
from .models import Episode, EpisodeChannel, EpisodeMentions
from .serializers import EpisodeSerializer, EpisodeChannelSerializer

from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from user_interface.models import ChannelOwner, Channel
from user_interface.serializers import ChannelSerializer

# Create your views here.

User = get_user_model()


class EpisodeModelView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all().order_by('title')


class NewEpisodeFormView(LoginRequiredMixin, FormView):
    form_class = EpisodeForm
    template_name = 'content/new_episode_form.html'
    login_url = '/login/'
    redirect_field_name = 'next'

    def channel_owner_info(self):
        user = User.objects.get(pk=self.request.user.pk)
        channel_owner = ChannelOwner.objects.get_or_none(user=user)

        return channel_owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channel_name'] = self.channel_owner_info().channel.name

        return context

    # @staticmethod
    # def clean_audio_file(form):
    #     file = form.cleaned_data.get('audio_file', False)
    #     if file:
    #         if file.content_type not in ['audio/mpeg', 'audio/mp4', 'audio/basic', 'audio/mp3']:
    #             raise ValidationError(
    #                 "Sorry, we do not support that audio MIME type. Please try uploading an mp3 file, or other common "
    #                 "audio type."
    #             )
    #
    #         if os.path.splitext(file.name)[1] not in ['.mp3', '.au', '.midi', '.ogg', '.ra', '.ram', '.wav']:
    #             raise ValidationError("Sorry, your audio file doesn't have a proper extension.")
    #
    #         file_content = file.read()
    #         mime_type = magic.from_buffer(file_content, mime=True)
    #         if not mime_type.startswith('audio'):
    #                 raise ValidationError("Not a valid audio file")
    #         else:
    #             raise ValidationError("Couldn't read uploaded file")
    #
    #     else:
    #         raise ValidationError("Couldn't read uploaded file")

    def form_valid(self, form):
        # self.clean_audio_file(form)
        episode = form.save()
        channel_owner = self.channel_owner_info()
        EpisodeChannel.objects.create(episode=episode, channel=channel_owner.channel)

        return redirect(f'mention/{episode.id}', permanent=True)


class EpisodeMentionsFormView(LoginRequiredMixin, FormView):
    form_class = EpisodeMentionsForm
    template_name = 'content/episode_mentions.html'
    login_url = '/login/'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['episode_name'] = Episode.objects.get(pk=self.kwargs['pk']).title

        return context

    def form_valid(self, form):
        channels = form.cleaned_data.get('channels')
        print(channels)
        episode = Episode.objects.get(pk=self.kwargs['pk'])
        mention, created = EpisodeMentions.objects.get_or_create(episode=episode)

        if created:
            if channels:
                new_mentions = ', '.join(str(mention) for mention in channels)
                response_text = (f"'{episode.title.capitalize()}' Episode Created Successfully "
                                 f"with '{new_mentions}' mentioned")

            else:
                response_text = (f"'{episode.title.capitalize()}' Episode Created Successfully "
                                 "with no channels mentioned")

        else:
            mentioned_channels = ', '.join(str(channel) for channel in mention.channel.all())
            response_text = (f"Channel(s) ({mentioned_channels}) is/are already mentioned for "
                             f"'{episode.title.capitalize()}'")

        return HttpResponse(response_text)


class ChannelEpisodesView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get(request, *args, **kwargs):
        channel_pk = kwargs.get('pk')

        try:
            channel = Channel.objects.get(pk=channel_pk)

        except Episode.DoesNotExist:
            return Response({'message': 'Channel NOT found'}, status=404)

        channel_data = ChannelSerializer(channel).data
        episodes = EpisodeChannel.objects.filter(channel=channel)
        channel_data['episodes'] = EpisodeChannelSerializer(episodes, many=True).data

        return Response(channel_data)


class EpisodeDownloadView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get(request, *args, **kwargs):
        episode = get_object_or_404(Episode, pk=kwargs.get('pk'))

        return FileResponse(episode.audio_file, as_attachment=True, filename=f"{episode.title}.mp3")


class AudioPlayerView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        audio = get_object_or_404(Episode, pk=kwargs.get('pk')).audio_file
        context = {'audio_file_url': audio.url}

        return render(request, 'content/play_audio.html', context)
