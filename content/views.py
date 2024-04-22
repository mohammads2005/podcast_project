from django.shortcuts import render, HttpResponse

from .forms import EpisodeForm
# from .models import Episode

# Create your views here.


def upload_new_podcast(request):
    if request.method == 'POST':
        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponse("File created successfully")

    else:
        form = EpisodeForm()

        return render(request, "content/new_episode_form.html", {'form': form})
