from django.urls import resolve, reverse
from rest_framework import serializers

from core.models import (
    Album,
    Artist,
    Genre,
    Language,
    Playlist,
    PlaylistItem,
    Song,
)


class ForeignKeySerializer(serializers.HyperlinkedRelatedField):
    def to_representation(self, instance):
        # request = self.context.get("request")
        # expand = request.query_params.get("expand", "") if request else ""
        # expand_fields = expand.split(",") if expand else []
        # if self.field_name in expand_fields:
        url = reverse(self.view_name, args=[instance.pk])
        resolver_match = resolve(url)
        view_class = resolver_match.func.view_class
        obj = view_class.queryset.get(pk=instance.pk)
        validated_data = view_class.serializer_class(obj, context=self.context).data

        return validated_data

        # url = super().to_representation(instance)
        # return {
        #     "id": instance.pk,
        #     "url": url,
        # }


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["name", "publication_year"]
        extra_kwargs = {
            "url": {
                "view_name": "album-detail-v1",
            }
        }


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "view_name": "artist-detail-v1",
            }
        }


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "view_name": "genre-detail-v1",
            }
        }


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "view_name": "language-detail-v1",
            }
        }


class SongSerializer(serializers.ModelSerializer):
    album = ForeignKeySerializer(view_name="album-detail-v1", read_only=True)
    artist = ForeignKeySerializer(view_name="artist-detail-v1", many=True, read_only=True)
    genre = ForeignKeySerializer(view_name="genre-detail-v1", many=True, read_only=True)
    language = ForeignKeySerializer(view_name="language-detail-v1", read_only=True)
    class Meta:
        model = Song
        fields = "__all__"

    def run_validation(self, attrs):
        errors = {}

        valid_artists = []
        artist = attrs.get("artist")
        if artist:
            artist_ids = [int(id) for id in artist.split(",")]
            artist_instances = Artist.objects.in_bulk(artist_ids)

            valid_artists = [
                artist_instances.get(id)
                for id in artist_ids
                if artist_instances.get(id)
            ]

            invalid_artist_ids = set(artist_ids) - set(artist_instances.keys())

            if invalid_artist_ids:
                errors["artists"] = (
                    f"Invalid artist id(s): {', '.join(map(str, invalid_artist_ids))}"
                )

            attrs["artist"] = valid_artists
        
        language_id = attrs.get("language")
        if language_id:
            language_instance = Language.objects.filter(id=language_id)
            if not language_instance.exists():
                errors["language"] = "Invalid language ID"
            else:
                attrs["language"] = language_instance.first()

        album_id = attrs.get("album")
        if album_id:
            album_instance = Language.objects.filter(id=album_id)
            if not album_instance.exists():
                errors["album"] = "Invalid album ID"
            else:
                attrs["album"] = album_instance.first()
        
        if errors:
            raise serializers.ValidationError
        
        return attrs


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "view_name": "playlist-detail-v1",
            }
        }


class PlaylistItemSerializer(serializers.ModelSerializer):
    song = ForeignKeySerializer(view_name="song-detail-v1", read_only=True)
    playlist = ForeignKeySerializer(view_name="playlist-detail-v1", read_only=True)
    class Meta:
        model = PlaylistItem
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "playlistitem-detail-v1"},
        }
    
    def run_validation(self, attrs):
        errors = {}
        if self.context["request"].method == "POST":
            required_fields = [
                "song",
                "playlist",
                "order",
            ]
            for field in required_fields:
                if not attrs.get(field) or attrs.get(field) is None:
                    errors[field] = f"{field} is required"
            if errors:
                raise serializers.ValidationError(errors)
        
        song_id = attrs.get("song")
        if song_id:
            song_instance = Song.objects.filter(id=song_id)
            if not song_instance.exists():
                errors["song"] = "Invalid song ID"
            else:
                attrs["song"] = song_instance.first()
        
        playlist_id = attrs.get("playlist")
        if playlist_id:
            playlist_instance = Playlist.objects.filter(id=playlist_id)
            if not playlist_instance.exists():
                errors["playlist"] = "Invalid playlist ID"
            else:
                attrs["playlist"] = playlist_instance.first()

        if errors:
            raise serializers.ValidationError(errors)
        
        return attrs
