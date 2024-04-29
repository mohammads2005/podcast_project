from django import forms

from content.models import Episode
# from user_interface.models import Channel


class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = (
            "title",
            "description",
            "audio_file",
            "image",
        )
