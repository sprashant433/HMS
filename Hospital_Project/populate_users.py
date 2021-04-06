import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Project.settings')

import django

django.setup()

from Hospital_app.models import Userinfo
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = fakegen.email()
        fake_id = fakegen.bothify(text='????-########')
        fake_username = fake_firstname[:3] + fake_lastname[:3]
        fake_pass = fakegen.lexify(text='??????????')
        fake_dob = fakegen.date()
        # new entry
        user = Userinfo.objects.get_or_create(
            Username=fake_username,
            Email=fake_email,
            First_Name=fake_firstname,
            Last_Name=fake_lastname,
            Password=fake_pass,
            uniqueID=fake_id,
            DOB=fake_dob

        )[0]


if __name__ == '__main__':
    print("Populating Databases")
    populate(10)
    print("Completed!")
