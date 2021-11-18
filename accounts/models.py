from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, unique=True)

    username = None
    fist_name=None
    last_name=None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    mobile = models.CharField(max_length=10, null=False)

    is_subscriber = models.BooleanField(default=False)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.name