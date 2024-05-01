from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import ChannelForm, CustomUserCreationForm
from .models import ChannelOwner, Channel
from .serializers import ChannelSerializer, CustomUserSerializer

from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


User = get_user_model()


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up/sign_up.html'


def new_channel(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES)
        if form.is_valid():
            created_channel = form.save()

            ChannelOwner.objects.create(
                channel=created_channel,
                user=User.objects.get(pk=request.user.pk),
                description=created_channel.description,
            )

            return HttpResponse(f"{form.cleaned_data['name']} channel is created!")

        else:
            return HttpResponse(form.errors)

    else:
        form = ChannelForm()

        return render(request, "new_channel/new_channel_form.html", {"form": form})


class ChannelsView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all().order_by('name')


class UserProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)


class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_serializer(self, *args, **kwargs):
        kwargs['exclude'] = ['last_login', 'date_joined']
        return CustomUserSerializer(*args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
