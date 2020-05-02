from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)    # here, we can have just a single line of text
    content = models.TextField()  # a textfield isfor unristricted text, i.e. we can have lines and lines of text
    date_posted = models.DateTimeField(default=timezone.now)
    # if the user whocreated the post gets deleted, then delete thier posts as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
