from rest_framework import serializers
from .models import *

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class PlaylistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        exclude = ['song']


class PlaylistReadSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True)
    class Meta:
        model = Playlist
        fields = "__all__"
