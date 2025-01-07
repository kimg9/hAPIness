from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    age = models.IntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(120)]
    )
    can_be_contacted = models.BooleanField(null=False, default=True)
    can_data_be_shared = models.BooleanField(null=False, default=True)
    # suscribed_project = models.ManyToManyField(null=True, to=Project)
