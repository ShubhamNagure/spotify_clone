from .models import Artist, Album, Track, Playlist
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class ArtistsSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class TrackSerializer(ModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'

class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
        read_only_fields = ('user_id',)

    def validate_name(self, value):
        if 'invalid' in value.lower():
            raise serializers.ValidationError("Playlist name cannot contain the word 'invalid'.")
        return value

    def validate(self, data):
        if data['collaborative'] and not data['public']:
            raise serializers.ValidationError("Collaborative playlists must be public.")
        return data