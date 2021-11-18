from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def get_all_categories(request):
    return HttpResponse("Category List")