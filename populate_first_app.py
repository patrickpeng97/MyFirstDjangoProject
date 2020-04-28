import os
import random
from faker import Faker
from first_app.models import AccessRecord, WebPage, Topic

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyFirstDjangoProject.settings")

import django

django.setup()

faker = Faker("zh_CN")
topics = ["Search", "Social", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get the topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = faker.url()
        fake_date = faker.date()
        fake_name = faker.company()

        # create the new web page entry
        web_page = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that web page
        acc_rec = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
