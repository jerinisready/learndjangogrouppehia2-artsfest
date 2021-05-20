from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            raw_password = request.POST['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'my_name': "Jerin"0

    }
    return render(request, 'registration/signup.html', context)


@login_required
def home_page(request):
    return HttpResponse("Welcome, " + request.user.username)


