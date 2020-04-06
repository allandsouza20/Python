from django.urls import path
from . import views         # . refers to the current directory

urlpatterns = [
    # Here, '' refers to an empty path. If it it an empty path, whenever you give the url as localhost:8000, it directs you directly to the homepage
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
