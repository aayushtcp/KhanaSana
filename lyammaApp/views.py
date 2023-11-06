from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PartnerRequest,launchPartner, AllItems,Contact
# Create your views here.

# For index Page / Landing Page / Home Page
def index(request):
    return render(request, 'chainekura.html')

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
        # myuser.is_staff = True
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

def partnerrequest(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        restaurantname = request.POST["restaurantname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        message = request.POST["message"]
        print(fullname, restaurantname, phone, email, message)
        # ==============At production remove print and un-comment below three lines===============================
        # partnerrequest = partnerrequest(
        #     fullname=fullname, restaurantname = restaurantname, phone=phone, email=email, message = message
        # )
        # partnerrequest.save()
        # =========================================================================================================
    return redirect("/")

def restaurantlist(request):
    approvedPartners = launchPartner.objects.all()
    # print(allItems)
    context = {"approvedPartners": approvedPartners}
    return render(request, 'restaurantlist.html', context)

def restaurantProfile(request,slug):
    partnersappro = launchPartner.objects.filter(slug=slug).first()
    context = {"partnersappro": partnersappro}
    return render(request, "restaurantProfile.html", context)

    # approvedPartners = launchPartner.objects.all()
    # print(approvedPartners)
    # context = {"approvedPartners": approvedPartners}
    # return render(request, 'fun.html', context)


def about(request):
    return render(request, 'about.html')


def contactus(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cphone = request.POST['cphone']
        content = request.POST['content']
        contact = Contact(cname=cname,cemail=cemail, cphone=cphone, content=content)
        print(contact)
        messages.success(request, "Message Received!")
        # contact.save()
    return render(request, 'contactus.html')