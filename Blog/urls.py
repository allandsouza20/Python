from django.urls import path
from . import views         # . refers to the current directory

urlpatterns = [
    path('', views.home, name='blog-home'),       # Here, '' refers to an empty path
    path('about/', views.about, name='blog-about'),
]
