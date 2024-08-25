import random
from django.contrib.auth import get_user_model
from movies.models import Movies

from .models import Rating,RatingChoice

User=get_user_model()

def generate_fake_reviews(count=100,users=10,null_avg=False):
    user_s=User.objects.first()
    user_e=User.objects.last()
    random_user_ids=random.sample(range(user_s.id,user_e.id),users)
    users=User.objects.filter(id__in=random_user_ids)
    movies=Movies.objects.all().order_by("?")[:count]
    if null_avg:
            movies=Movies.objects.filter(rating_avg__isnull=True).order_by("?")[:count]
    n_rating=movies.count()
    rating_choices =[x for x in RatingChoice.values if x is not None]
    user_ratings=[random.choice(rating_choices) for _ in range(n_rating)]
    new_ratings=[]
    for movie in movies:
        rating_obj=Rating.objects.create(
                content_object=movie,
                value=user_ratings.pop(),
                user=random.choice(users),
          )
        new_ratings.append(rating_obj)
    return new_ratings





