from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)        # create a form that has the request.POST data
        if form.is_valid():
            # if the data is valid
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


# Types of messages
# message.debug
# message.info
# message.warning
# message.success
# message.error
