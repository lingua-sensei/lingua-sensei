from rest_framework import serializers
from linguist.models import Audio


class BasicAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ("id", "text", "language", "file")


class AudioSerializer(serializers.ModelSerializer):
    linked_audios = serializers.SerializerMethodField()

    class Meta:
        model = Audio
        fields = ("id", "text", "language", "file", "correspondent_text", "correspondent_language", "linked_audios")

    def get_linked_audios(self, obj):
        return BasicAudioSerializer(
            obj.linked_audios.order_by("?"),  # shuffle
            many=True,
        ).data
