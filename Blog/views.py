from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.http import HttpResponse
from .models import Post  # from the models file in the current package import that Post data
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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


class PostListView(ListView):
    # this tells the list what model to query in order to create the list. In this case, it will be all of our posts.
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    # this tells the list what model to query in order to create the list. In this case, it will be all of our posts.
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # this tells the list what model to query in order to create the list. In this case, it will be all of our posts.
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # this tells the list what model to query in order to create the list. In this case, it will be all of our posts.
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:     # if the current user is the author of the post
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # this tells the list what model to query in order to create the list. In this case, it will be all of our posts.
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:     # if the current user is the author of the post
            return True
        return False


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
