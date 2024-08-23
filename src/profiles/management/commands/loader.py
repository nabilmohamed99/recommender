from django.core.management import BaseCommand
from django.contrib.auth import get_user_model

from recommender import utils as recommender_utils
from movies.models import Movies

User = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.add_argument("--count", type=int, default=10)
        parser.add_argument("--show-total", action="store_true", default=False)
        parser.add_argument("--movies", action="store_true", default=False)

        parser.add_argument("--users", action="store_true", default=False)


    def handle(self, *args, **options):
        count = options.get("count")
        show_total = options.get("show_total")
        movies=options.get("movies")
        fake_users = options.get("users")
        if movies:
           movies_dataset = recommender_utils.load_movie_metadata(limit=count)
           print(movies_dataset)
           movies_new=[Movies(**data) for data in movies_dataset]
           print(movies_new)
           movies_bulck=Movies.objects.bulk_create(movies_new,ignore_conflicts=True)
           print(f"Créé {len(movies_bulck)} nouveaux films")
           if show_total:
                final_movie_count=Movies.objects.count()
                print(f"Nombre total de films : {final_movie_count}")
        if fake_users:
            initial_user_count = User.objects.count()
            print(f"Nombre initial d'utilisateurs : {initial_user_count}")

            profiles = recommender_utils.get_fake_profiles(count=count)
            new_users = []

            for profile in profiles:
                # Créer un dictionnaire avec uniquement les champs pertinents
                user_data = {
                    'username': profile['username'],
                    'email': profile.get('email'),
                    'is_active': True,
                    'first_name': profile.get('first_name'),
                    'last_name': profile.get('last_name'),
                }
                new_users.append(User(**user_data))

            # Créer les utilisateurs en une seule transaction
            User.objects.bulk_create(new_users, ignore_conflicts=True)
            print(f"Créé {count} nouveaux utilisateurs")

        if show_total:
            final_user_count = User.objects.count()
            print(f"Nombre total d'utilisateurs : {final_user_count}")


