from django.db import models
import datetime

# Create your models here.
class Library(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=datetime.date.today)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)