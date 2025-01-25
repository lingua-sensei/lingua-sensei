from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from linguist.models import Audio
from linguist.serializers import AudioSerializer


class AudioPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class AudioListView(generics.ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    pagination_class = AudioPagination


class AudioDetailView(generics.RetrieveAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    lookup_field = "id"
