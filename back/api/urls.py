from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # user urls come from djoser
    path('movies/', views.MovieList.as_view(), name='movies'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),  
    path('genres/', views.GenreList.as_view(), name='genre-list'),
    path('genres/<pk>/', views.GenreDetail.as_view(), name='genre-detail'),
    path('ratings/', views.RatingList.as_view(), name='rating-list'),
    path('ratings/<pk>/', views.RatingDetail.as_view(), name='rating-detail'),
    path('watched/', views.WatchedList.as_view(), name='watched-list'),
    path('watched/<pk>/', views.WatchedDetail.as_view(), name='watched-detail'),
    path('wishlist/', views.WishlistList.as_view(), name='wishlist-list'),
    path('wishlist/<pk>/', views.WishlistDetail.as_view(), name='wishlist-detail'),
    path('movies/search/', views.MovieSearch.as_view(), name='movie-search'),
]
urlpatterns = format_suffix_patterns(urlpatterns)