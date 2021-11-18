from django.db import models
from django.db.models.base import Model
from category.models import Category
# Create your models here.

class Book(models.Model):
    # TODO: change book id to autofield
    book_id = models.CharField(primary_key=True,max_length=250)
    title = models.CharField(max_length=250)
    tagline = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)

    options = [
        ('ebook','ebook'),('audiobook','audiobook')
    ]

    type = models.CharField(max_length=250, choices=options)
    file_url = models.FileField(upload_to='media/book/')
    thumbnail = models.ImageField(upload_to='media/thumbnails/')
    # tagline = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title