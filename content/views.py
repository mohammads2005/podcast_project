from django.shortcuts import render, HttpResponse

from .forms import EpisodeForm
from .models import Episode
from .serializers import EpisodeSerializer

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response


# Create your views here.


class EpisodeModelView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all().order_by('id')

    def create(self, request, *args, **kwargs):
        return Response({"detail": "POST method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def post(request, *args, **kwargs):
    #     return Response({"detail": "POST method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def upload_new_podcast(request):
    if request.method == 'POST':
        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponse("File created successfully")

    else:
        form = EpisodeForm()

        return render(request, "content/new_episode_form.html", {'form': form})
