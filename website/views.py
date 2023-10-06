from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    # Check to see if logging in
    if request.method == "POST":
        # Get the username and password
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        # Check if the user is valid
        if user is not None:
            # Log them in
            login(request, user)
            # Redirect them to the home page
            messages.success(request, "Successfully logged in")
            return redirect("home")
        else:
            # Send an error message
            messages.error(request, "Invalid username or password")
            return redirect("home")
    else:
        return render(request, "home.html", {})


def logout_user(request):
    pass
