from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    age = models.IntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(120)]
    )
    can_be_contacted = models.BooleanField(null=False, default=True)
    can_data_be_shared = models.BooleanField(null=False, default=True)
