from django.shortcuts import render

from django.contrib.auth import login, authenticate
# Create your views here.
from . forms import LoginForm

def user_login(request):
    if request.method == "POST":
        user_form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],
                                password = cd['password'])
            if user is None:
                if user.is_active():
                    login(request, user)
                else:
                    HttpResponse("Disabled Account")
            else:
                HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    request render(request, 'accounts/login.html', {'form':form})
