from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from linguist.core.models import Audio
from linguist.core.serializers import AudioSerializer


class AudioPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AudioView(generics.ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    pagination_class = AudioPagination
