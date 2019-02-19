from django.shortcuts import render

from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from . forms import LoginForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("blog:quotes")
    else:
        form = UserCreationForm()
        return render(request, "registration/register.html")


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
    return render(request, 'accounts/login.html', {'form':form})
