from .models import Artist,Album, Track, Playlist
from .serializers import ArtistsSerializer,AlbumSerializer, TrackSerializer, PlaylistSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class tracksView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [IsAuthenticated]

class trackDetailView(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [IsAuthenticated]


class ArtistsView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer
    permission_classes = [IsAuthenticated]

class ArtistDetailView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer
    permission_classes = [IsAuthenticated]

class AlbumsView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

class AlbumDetailView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

class PlaylistView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # permission_classes = [IsAuthenticated]