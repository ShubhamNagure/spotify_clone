from .models import Artist, Album, Track
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
