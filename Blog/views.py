from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post  # from the models file in the current package import that Post data
# This is a list of dictionaries
# posts = [
#     {
#         'author': 'Allan',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
# ]
# function to handle traffic from the homepage of our blog


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
