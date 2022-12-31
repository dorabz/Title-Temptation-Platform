from rest_framework import serializers
from api.models import Movie, Genre, Rating, Watched, Wishlist

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = [
            'id',
            'added_at',
            'title',
            'description',
            'release_year',
            'duration',
            'imdb_rating',
            'users_rating',
            'genres'
        ]

class RatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = ['id', 'user', 'movie', 'rating']

class WatchedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watched
        fields = ['id', 'user', 'movie']

class WishlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'movie']

