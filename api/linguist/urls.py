from django.urls import path

from linguist.views import AudioListView, AudioDetailView

urlpatterns = [
    path("audios/", AudioListView.as_view(), name="audio_list"),
    path("audios/<int:id>/", AudioDetailView.as_view(), name="audio-detail"),
]
