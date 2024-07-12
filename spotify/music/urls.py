from django.urls import path
from .views import tracksView, trackDetailView, ArtistsView, ArtistDetailView, \
                    AlbumsView, AlbumDetailView, PlaylistView

urlpatterns = [
    path('tracks/', tracksView.as_view(), name='tracks' ),
    path('tracks/<int:pk>/', trackDetailView.as_view(), name='track' ),
    path('artists/', ArtistsView.as_view(), name='artists' ),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist' ),
    path('albums/', AlbumsView.as_view(), name='artist' ),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='artist' ),
    path('playlists/', PlaylistView.as_view(), name='playlists' ),
]   
