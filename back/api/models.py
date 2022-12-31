from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, DecimalField

class Genre(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    added_at = models.DateTimeField(auto_now_add=True)
    #slug = models.SlugField(unique=True, prepopulate_from='title')

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    release_year = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    #users_rating = models.DecimalField(decimal_places=1, max_digits=2)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


    @property
    def userrating_set(self):
        return self.rating_set.all()

    @property
    def users_rating(self):
        ratings = self.userrating_set.all()
        if ratings.count() == 0:
            return DecimalField(decimal_places=1, max_digits=3).to_python(0)
        return DecimalField(decimal_places=1, max_digits=3).to_python(ratings.aggregate(Avg('rating'))['rating__avg'])



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=3)

    class Meta:
        unique_together = ['user', 'movie']


class Watched(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'movie')


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ('user', 'movie')


#class MovieSuggestion(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    title = models.CharField(max_length=200)
#    description = models.TextField(max_length=1000)
#    release_year = models.PositiveSmallIntegerField()
#    imdb_rating = models.DecimalField(max_digits=2, decimal_places=1)
#    genres = models.ManyToManyField(Genre)
#    created_at = models.DateTimeField(auto_now_add=True)