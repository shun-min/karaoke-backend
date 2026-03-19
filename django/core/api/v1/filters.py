from django.db.models import QuerySet
from django_filters import rest_framework
from django_filters import rest_framework as filters

from core.models import (
    Song,
)


class SongFilter(rest_framework.FilterSet):
    language = filters.NumberFilter(
        method="getSongByLanguage",
        label="Song Language",
        distinct=True,
    )
    artist = filters.NumberFilter(
        method="getSongByArtist",
        label="Song Artist",
        distinct=True,
    )
    genre = filters.NumberFilter(
        method="getSongByGenre",
        label="Song Genre",
        distinct=True,
    )
    album = filters.NumberFilter(
        method="getSongByAlbum",
        label="Song Album",
        distinct=True,
    )
    

    class Meta:
        model = Song
        fields = [
            'name',
        ]

    def getSongByLanguage(self, queryset: QuerySet, name, value: int):
        return queryset.filter(language__id=value)
        
    def getSongByArtist(self, queryset: QuerySet, name, value: int):
        return queryset.filter(artist__id=value)
    
    def getSongByGenre(self, queryset: QuerySet, name, value: int):
        return queryset.filter(genre__id=value)

    def getSongByAlbum(self, queryset: QuerySet, name, value: int):
        return queryset.filter(album__id=value)
