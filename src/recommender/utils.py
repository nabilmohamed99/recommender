
from faker import Faker
import csv
from pprint import pprint
from django.conf import settings
import datetime

def validate_date_str(date_text):
    try:
        date_text=datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except:
        return None
    return date_text


MOVIE_METADATA_CSV = settings.DATA_DIR /"movies_metadata.csv"
fake = Faker()


def load_movie_metadata(limit=10):
    with open(MOVIE_METADATA_CSV,newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        dataset=[]


        for i ,row in enumerate(reader):
            _id=row.get("id")
            try:
                _id = int(_id)
            except:

                _id = None
            release_date = validate_date_str(row.get("release_date"))
            print(release_date)
            data= {
                "id": _id,
                "title": row.get("title"),
                "overview": row.get("overview"),
                "release_date": release_date,



            }
            dataset.append(data)

            if i >= limit:
                break
            #pprint(row)
        return dataset


def get_fake_profiles(count=10):
    faker = Faker()
    user_data = []
    for _ in range(count):
        profile = faker.profile()
        name_parts = profile.get('name').split(" ")
        first_name = name_parts[0] if len(name_parts) > 0 else ""
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        data = {
            'username': profile['username'],
            'email': profile.get('mail'),
            'first_name': first_name,
            'last_name': last_name,
        }
        user_data.append(data)
    return user_data