from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    gender_choice = (
        ('male', '男'),
        ('female', '女'),
    )
    gender = models.CharField(choices=gender_choice, default='male', max_length=16)
