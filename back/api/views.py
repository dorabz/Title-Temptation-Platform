from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination

from api import serializers
from api.models import Movie, Genre, Rating, Watched, Wishlist

from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class MoviePagination(PageNumberPagination):
    page_size = 2

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    pagination_class = MoviePagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'genres__name')

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer


class WatchedList(generics.ListCreateAPIView):
    queryset = Watched.objects.all()
    serializer_class = serializers.WatchedSerializer

    def get(self, request, format=None):
        # Get the user id from the query parameters
        user_id = request.query_params.get('user')

        # Filter the Wishlist objects by the user id
        watched = Watched.objects.filter(user=user_id)

        # Serialize the list of Wishlist objects and return the response
        serializer = serializers.WatchedSerializer(watched, many=True)
        return Response(serializer.data)

class WatchedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watched.objects.all()
    serializer_class = serializers.WatchedSerializer

    def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class WishlistList(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer

    def get(self, request, format=None):
        # Get the user id from the query parameters
        user_id = request.query_params.get('user')

        # Filter the Wishlist objects by the user id
        wishlist = Wishlist.objects.filter(user=user_id)

        # Serialize the list of Wishlist objects and return the response
        serializer = serializers.WishlistSerializer(wishlist, many=True)
        return Response(serializer.data)

class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def delete(self, request, pk, format=None):
        wishlist = get_object_or_404(Wishlist, pk=pk)
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieSearch(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if query is not None:
            movies = Movie.objects.filter(title__icontains=query)
            serializer = serializers.MovieSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Please provide a search query'})  
