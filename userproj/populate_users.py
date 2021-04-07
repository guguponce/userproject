import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','userproj.settings')

import django
django.setup()

import random
from users.models import Usuarios
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_nombre = fake_name[0]
        fake_apellido = fake_name[1]
        fake_email = fakegen.email()

        usua = Usuarios.objects.get_or_create(first_name=fake_nombre,
                                              last_name=fake_apellido,
                                              email=fake_email)



if __name__ == '__main__':
    print('populating')
    populate(10)
    print('populated')
