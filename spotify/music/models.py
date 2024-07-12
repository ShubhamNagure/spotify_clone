from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User
# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='Albums')
    dor = models.DateField()
    
    def __str__(self) -> str:
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='Tracks')
    duration = models.DurationField(default=timedelta())

    def __str__(self) -> str:
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description= models.TextField()
    collaborative= models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Playlists')
    track = models.ManyToManyField(Track,related_name='Playlists')

    def __str__(self) -> str:
        return self.name