from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_enrollment, name="new_enrollment"),
    path('mybooks', views.my_book, name='my_book'),
    path('currentreading/<str:bookId>', views.current_book, name='current_book'),
    path('updatepage/<str:bookId>/<int:pageNum>',views.update_current_page, name="update_page")
]