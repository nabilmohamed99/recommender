from django.db import models

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Rating(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    __empty__ = 'Not Rated'

User = settings.AUTH_USER_MODEL # 'auth.User'
# user_ratings = user_obj.rating_set.all()
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value= models.IntegerField(null=True,blank=True,choices=Rating.choices)
    content_type=   models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id=  models.PositiveIntegerField() #UUIDField(primary_key=True) il va pas fonctionner
    content_object= GenericForeignKey('content_type','object_id')
    timestamp=  models.DateTimeField(auto_now_add=True)
    active= models.BooleanField(default=True)
    


