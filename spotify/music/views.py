from django.shortcuts import render
from .models import Artist,Album, Track
from .serializers import ArtistsSerializer,AlbumSerializer, TrackSerializer
from rest_framework import generics


class tracksView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class trackDetailView(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class ArtistsView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer

class ArtistDetailView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer

class AlbumsView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

