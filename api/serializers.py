from rest_framework import serializers
from .models import Video


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class SaveVideoSerializer(serializers.Serializer):

    class Meta:
        model = Video
        fields = "__all__"

class VideoSerializer(serializers.Serializer):

    class Meta:
        model = Video
        fields = ('id', 'VideoLink', 'duration', 'thumb',
                  'embed_code', 'tags', 'quality')
