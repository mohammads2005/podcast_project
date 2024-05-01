from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Channel


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'profile_picture', 'bio', 'social_link')

    profile_picture = forms.ImageField(label='Profile Picture', required=False)
    bio = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    social_link = forms.URLField(label='Social Link', required=False)


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('name', 'logo', 'description')
