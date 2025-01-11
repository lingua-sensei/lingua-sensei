from django.urls import path

from linguist.core.views import AudioView

urlpatterns = [
    path("", AudioView.as_view(), name="audio_list"),
]