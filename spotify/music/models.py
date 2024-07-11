from django.db import models
from datetime import timedelta
# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()

    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='Album')
    dor = models.DateField()
    
    def __str__(self) -> str:
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=60)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='Track')
    duration = models.DurationField(default=timedelta())

    def __str__(self) -> str:
        return self.title

    