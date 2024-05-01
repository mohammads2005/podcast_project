from django import forms

from .models import Episode, EpisodeMentions

from user_interface.models import Channel


class EpisodeForm(forms.ModelForm):

    class Meta:
        model = Episode
        fields = (
            "title",
            "description",
            "audio_file",
            "image",
        )


class EpisodeMentionsForm(forms.ModelForm):
    channels = forms.ModelMultipleChoiceField(
        queryset=Channel.objects.all(),
        required=False,
    )

    class Meta:
        model = EpisodeMentions
        fields = ('channels',)
