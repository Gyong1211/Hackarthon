from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class MyUser(AbstractUser):

    nickname = models.CharField(max_length=24, null=True, unique=True)
    mobile = models.CharField(max_length=11)
    img_profile = models.ImageField(upload_to='user',
                                    blank=True,
                                    )

    def __str__(self):
        return self.nickname or self.username


