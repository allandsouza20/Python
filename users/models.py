from django.db import models
from django.contrib.auth.models import User  # extend the existing user model that django provides us


class Profile(models.Model):
    # specifies the user for the profile. on_delete tells django what we want to do with the profile when it is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # specifies the profile picture
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
