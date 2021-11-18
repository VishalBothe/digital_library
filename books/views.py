from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Book
# Create your views here.

def all_books(request):
    books = Book.objects.all()
    return render(
        request,
        'books/all_books.html',
        {"books":books}
    )