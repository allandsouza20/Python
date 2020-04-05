from django.shortcuts import render
from django.http import HttpResponse

# function to handle traffic from the homepage of our blog


def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
