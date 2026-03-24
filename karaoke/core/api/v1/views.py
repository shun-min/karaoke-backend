from rest_framework import generics, status
from rest_framework.response import Response

from core.api.v1.filters import (
    SongFilter,
)
from core.api.v1.serializers import (
    AlbumSerializer,
    ArtistSerializer,
    GenreSerializer,
    LanguageSerializer,
    PlaylistItemSerializer,
    PlaylistSerializer,
    SongSerializer,
)
from core.models import (
    Album,
    Artist,
    Genre,
    Language,
    Playlist,
    PlaylistItem,
    Song,
)


class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by("id")
    serializer_class = AlbumSerializer
    filterset_fields = ['name']
    pagination_class = None


class AlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by("id")
    serializer_class = AlbumSerializer
    filterset_fields = ['name']
    pagination_class = None


class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all().order_by("id")
    serializer_class = ArtistSerializer
    filterset_fields = ['name']
    pagination_class = None


class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all().order_by("id")
    serializer_class = ArtistSerializer
    filterset_fields = ['name']
    pagination_class = None


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all().order_by("id")
    serializer_class = GenreSerializer
    filterset_fields = ['name']
    pagination_class = None


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all().order_by("id")
    serializer_class = GenreSerializer
    filterset_fields = ['name']
    pagination_class = None


class LanguageListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all().order_by("id")
    serializer_class = LanguageSerializer
    filterset_fields = ['name']
    pagination_class = None


class LanguageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all().order_by("id")
    serializer_class = LanguageSerializer
    filterset_fields = ['name']
    pagination_class = None


class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all().order_by("id")
    serializer_class = SongSerializer
    filterset_class = SongFilter
    # filterset_fields = ['name']
    pagination_class = None


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all().order_by("id")
    serializer_class = SongSerializer
    filterset_fields = ['name']
    pagination_class = None


class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all().order_by("id")
    serializer_class = PlaylistSerializer
    filterset_fields = ['name']
    pagination_class = None


class PlaylistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all().order_by("id")
    serializer_class = PlaylistSerializer
    filterset_fields = ['name']
    pagination_class = None


class PlaylistItemListCreateView(generics.ListCreateAPIView):
    queryset = PlaylistItem.objects.all().order_by("id")
    serializer_class = PlaylistItemSerializer
    filterset_fields = ['playlist__id']
    pagination_class = None


class PlaylistItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistItem.objects.all().order_by("id")
    serializer_class = PlaylistItemSerializer
    pagination_class = None

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_id = instance.id
        instance.delete()
        data = {
            "message": f"Object with ID {instance_id} has been deleted. "
        }

        return Response(data, status=status.HTTP_204_NO_CONTENT)
