from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pre_payment, name="payment"),
    path('post-payment/<str:duration>', views.post_payment, name="post_payment")
]