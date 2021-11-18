from django.db import models
from django.db.models.base import Model
from accounts.models import CustomUser
from books.models import Book 

# Create your models here.

class Enrollment(models.Model):
    enrollment_id = models.CharField(primary_key=True,max_length=250)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    current_page = models.IntegerField(default=0)
    total_page = models.IntegerField(default=0)

    def __str__(self):
        return self.enrollment_id