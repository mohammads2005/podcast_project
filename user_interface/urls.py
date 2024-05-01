from django.urls import path

from .views import SignUpView, UserProfileView, UserProfileUpdateView, new_channel


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='update'),
    path('new_channel/', new_channel, name='new_channel'),
]
