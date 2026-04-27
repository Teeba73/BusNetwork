from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required



@login_required(login_url='Users:login')
def index(request):
    booked_routes = request.user.routes.all()
    return render(request, 'Users/user.html', {
        'booked_routes': booked_routes
    })


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        confirmation = request.POST.get("confirmation", "")

        if password != confirmation:
            return render(request, "Users/register.html", {
                "message": "Oops! Seems like your fingers slipped. Your passwords don't match!"
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("Users:index"))
        except IntegrityError:
            return render(request, "Users/register.html", {
                "message": "Username already taken, try another."
            })

    return render(request, "Users/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("Users:index"))
        else:
            return render(request, "Users/login.html", {
                "message": "Wait... do I know you? Those credentials don't ring a bell!"
            })

    return render(request, "Users/login.html")


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return HttpResponseRedirect(reverse('Users:login'))