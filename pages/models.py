from django.db import models
from datetime import timedelta

class Listing(models.Model):

    movie_name = models.CharField(max_length=200)
    duration = models.IntegerField()
    description = models.TextField(max_length=500)
    user_ratings = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    genre = models.CharField(max_length=200)
    language = models.CharField(max_length=200)


    
    def __str__(self):
        return self.movie_name
