from django.core.management import BaseCommand
from django.contrib.auth import get_user_model

from recommender import utils as recommender_utils
from movies.models import Movies

from ratings.tasks import generate_fake_reviews
User = get_user_model()
from ratings.models import Rating

class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.add_argument("--count", type=int, default=10)
        parser.add_argument("--users", default=10000,type=int)
        parser.add_argument("--show_total", action="store_true", default=False)




    def handle(self, *args, **options):
        count = options.get("count")
        show_total = options.get("show_total")
        users_count=options.get("users")
        print(count,show_total,users_count)
        new_ratings=generate_fake_reviews(count=count,users=users_count)
        if show_total:
            qs=Rating.objects.all()
            print("total ratings",qs.count())


