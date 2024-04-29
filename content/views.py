from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView

from .forms import EpisodeForm
from .models import Episode
from .serializers import EpisodeSerializer

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from user_interface.models import ChannelOwner

# Create your views here.

User = get_user_model()


class EpisodeModelView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all().order_by('id')

    def create(self, request, *args, **kwargs):
        return Response({"detail": "POST method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "PUT method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class NewEpisodeFormView(LoginRequiredMixin, FormView):
    form_class = EpisodeForm
    template_name = 'content/new_episode_form.html'
    success_url = 'new_podcast_success/'
    login_url = '/login/'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        channel_owner = ChannelOwner.objects.get_or_none(user=user)

        context = super().get_context_data(**kwargs)
        context['channel_name'] = channel_owner.channel.name

        return context

    def form_valid(self, form):
        title = form.cleaned_data.get('title')

        return HttpResponse(f"{title.capitalize()} Episode Created Successfully")
