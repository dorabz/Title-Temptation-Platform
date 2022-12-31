from django.contrib import admin
from .models import Movie, Genre, Rating, Watched, Wishlist

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'duration', 'imdb_rating', 'users_rating')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Watched)
admin.site.register(Wishlist)
