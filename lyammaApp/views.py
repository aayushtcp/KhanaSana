from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

#For index Page / Landing Page / Home Page
def index(request):
    return render(request, 'index.html')

def handleSignup(request):
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        #Check for errors
        #
        #Create the user
        myuser = User.objects.create_user(username,email,password)
        myuser.save();
        messages.success(request, 'Your account has been successfully created!');
        return redirect('/')
    else:
        return HttpResponse("404-Not Allowed") 