from django.urls import path

from linguist.views import AudioView

urlpatterns = [
    path("audios/", AudioView.as_view(), name="audio_list"),
]
