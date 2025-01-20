from django.urls import path, include

from linguist.views import AudioView

urlpatterns = [
    path("audios/", AudioView.as_view(), name="audio_list"),
    path('api-auth/', include('rest_framework.urls')),
]
