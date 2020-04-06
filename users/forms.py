from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):       # Here, UserRegisterForm inherits from UserCreationForm
    email = forms.EmailField()  # it takes an arguement called required, by default, required is set to True

    class Meta:
        model = User  # whenever this form validates, it is going to create a new user
        fields = ['username', 'email', 'password1', 'password2']
# Here the class Meta gives us a nested namespace for configurations and keeps the configurations in one place
# and within the configuration we are saying that the model that will be affected is the user model, for example when we do a form.save(), it is going to save it to the user model
