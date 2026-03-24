from django.db import models


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    publication_year = models.IntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(
        Album,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    artist = models.ManyToManyField(
        Artist,
        related_name="+",
    )
    genre = models.ManyToManyField(
        Genre,
        related_name="+",
    )
    hitcounts = models.IntegerField(default=0)
    language = models.ForeignKey(
        Language,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    with_voice = models.BooleanField(
        default=False,
    )
    path = models.TextField(
        null=True,
        blank=True,
    )
    youtube_link = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ('name', 'album')
    
    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=50,
        default="Recent",
    )
    def __str__(self):
        return self.name


class PlaylistItem(models.Model):
    song = models.ForeignKey(
        Song,
        on_delete=models.PROTECT,
    )
    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    order = models.IntegerField(
        default=1,
    )

    class Meta:
        unique_together = ('playlist', 'order')
    
    def __str__(self):
        return str(f"{self.song.name} - {self.order}")
