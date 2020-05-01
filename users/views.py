from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)        # create a form that has the request.POST data
        if form.is_valid():
            # if the data is valid
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required      # This specifies a decorator. A decorator adds functionality to an existing function, and in this case it adds functionality to our profile view where the user must be logged in to view this page
def profile(request):
    return render(request, 'users/profile.html')

# Types of messages
# message.debug
# message.info
# message.warning
# message.success
# message.error
