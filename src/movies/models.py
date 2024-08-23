from django.db import models

# Create your models here.
from ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation

class Movies(models.Model):
    title = models.CharField(max_length=120,unique=True)
    overview = models.TextField()
    release_date = models.DateField(blank=True,auto_now=False,auto_now_add=
                                    False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings=GenericRelation(Rating) #queryset generic key reverse relationship
    def calculate_ratings_count(self):
        return self.ratings.all().count()

    def calculate_rating_avg(self):
        retrun self.ratings.all().count()
