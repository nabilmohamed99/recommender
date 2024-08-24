from django.db import models
import datetime
# Create your models here.
from ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone

RATING_CALC_TIME = 1 # minutes

class Movies(models.Model):
    title = models.CharField(max_length=120,unique=True)
    overview = models.TextField()
    release_date = models.DateField(blank=True,auto_now=False,auto_now_add=
                                    False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings=GenericRelation(Rating) #queryset generic key reverse relationship

    rating_last_updated = models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)


    rating_count = models.IntegerField(blank=True,null=True) # 5.00

    rating_avg = models.DecimalField(decimal_places=2, max_digits=5,blank=True,null=True) # 5.00

    def rating_avg_display(self):
        now= timezone.now()
        if not self.rating_last_updated:
            return self.caclulate_rating()

        if now> now- datetime.timedelta(minutes=RATING_CALC_TIME) :
            return self.rating_avg

        return self.caclulate_rating()

    def calculate_ratings_count(self):
        return self.ratings.all().count()

    def calculate_rating_avg(self):
        return self.ratings.all().avg()

    def caclulate_rating(self,save=True,force=True):
        rating_avg=self.caclulate_rating_avg()
        rating_count=self.caclulate_rating_count()
        self.rating_avg=rating_avg
        self.rating_count=rating_count
        self.rating_last_updated=timezone.now()
        if save:
            self.save()
        return rating_avg
