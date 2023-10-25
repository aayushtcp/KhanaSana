from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# For index Page / Landing Page / Home Page


def index(request):
    return render(request, 'index.html')


def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # Check for errors
        if len(username) > 10:
            messages.warning(
                request, "Username length must be less than 10 characters!")
            return redirect("/")

        if not username.isalnum():
            messages.success(
                request, "Username should only contain letters and numbers!")
            return redirect("/")

        if password != cpassword:
            messages.error(request, "Password do not match!")
            return redirect("/")

        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(
            request, 'Your account has been successfully created!')
        print(f"Hello {username}")
        return redirect('/')
    else:
        return HttpResponse("404-Not Allowed")
    



def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginUsername = request.POST['loginusername']
        loginPassword = request.POST['loginpassword']

        user = authenticate(username=loginUsername, password=loginPassword)

        if user is not None:
            login(request, user)
            messages.success(
                request, "Sucessfully Logged in!")
            return redirect("/")  # redirect on home
        else:
            messages.error(
                request, "Invalid credentials, Please try again!")
            return redirect("/")  # redirect on home
    return HttpResponse('$404- dont try be cool!')
    # Check for errors


def handleLogout(request):
    logout(request)
    messages.success(
        request, "You are Logged Out!")
    return redirect("/")  # redirect on home