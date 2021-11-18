from django.db import models
from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from books.models import Book
from .models import Enrollment

from datetime import date
import json
import uuid

from PyPDF2 import PdfFileReader

# Create your views here.

def new_enrollment(request):
    user = request.user

    if user.is_authenticated and not user.is_subscriber:
        return redirect('/payment/')

    if user.is_authenticated and request.method == "POST":
        book_id = request.POST['bookId']
        book = Book.objects.get(book_id=book_id)

        if Enrollment.objects.filter(book=book,user=user).exists():
            messages.info(request, 'You have already enrolled for this book')
            return redirect('/enrollment/mybooks')
        try:
            path = str(book.file_url)
            pdf = PdfFileReader(open(path,'rb'))
            numPages = pdf.getNumPages()

            enrollment_id = str(uuid.uuid1())
            enrollment = Enrollment(
                enrollment_id=enrollment_id,
                book=book,
                user=user,
                total_page=numPages
            )
            enrollment.save()
            messages.info(request, "Added to your books!!")
            return redirect('/enrollment/mybooks')
            
        except Exception as e:
            print("+++ ERROR OCCURED +++",e)
            return HttpResponse("<h1>Something went wrong!!</h1>")
    
    messages.info(request, "Login to continue!!")
    return redirect('/accounts/signin')

def my_book(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/signin')
    
    user = request.user

    sql = f'SELECT b.book_id,title,tagline,author,type,file_url,thumbnail,current_page,total_page \
    FROM books_book b, accounts_customuser u, enrollment_enrollment e \
    WHERE u.id = e.user_id and e.book_id=b.book_id and u.id={user.id};'

    my_books = Book.objects.raw(sql)
    have_books = True if len(my_books)>0 else False

    accessible = True if user.due_date is not None and date.today() <= user.due_date else False

    return render(request, 'enrollments/my_books.html',{"have_books":have_books,"my_books":my_books,"accessible":accessible})

def current_book(request, bookId):
    user = request.user
    accessible = True if date.today()<=user.due_date else False

    if user.is_authenticated and accessible:
        sql = f"SELECT book_id,file_url,current_page \
        FROM books_book join enrollment_enrollment \
        USING(book_id) WHERE book_id = '{bookId}'"

        book = Book.objects.raw(sql)[0]

        return render(request, 'enrollments/current_book.html', {"book":book})

    else:
        return HttpResponse("<center><h1>Something went wrong!!</h1></center>")


def update_current_page(request, bookId, pageNum):
    if request.user.is_authenticated:
        enrolment = Enrollment.objects.get(
            book=Book.objects.get(book_id=bookId),
            user=request.user
        )
        enrolment.current_page = pageNum
        enrolment.save()
    return HttpResponse(json.dumps({"status":200}))