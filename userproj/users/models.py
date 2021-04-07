from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuarios(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254,unique=True)

    def __str__(self):
        return self.email

class Comments(models.Model):
    nombre = models.CharField(max_length=30)
    comentario = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre


class UserProfileData(models.Model):
    user = models.OneToOneField(User)

    profile_URL = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images',blank=True)

    def __str__(self):
        return self.user.username
