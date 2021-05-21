from django.db import models
import datetime

# Create your models here.
class Library(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    description = models.TextField()

    def buy_movie(self):
        self.save()