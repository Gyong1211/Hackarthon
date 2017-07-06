from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    if __name__ == '__main__':
        img_profile = models.ImageField(upload_to='user', blank=True)
