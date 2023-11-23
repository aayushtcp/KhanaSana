from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import uuid 
from .models import PartnerRequest,launchPartner, AllItems,Contact

# also for payment gateway
from django.urls import reverse, reverse_lazy
from django.views import View

# esewa
import requests as req
# Create your views here.

# Hash secret  key esewa integration V2
import hmac
import hashlib
import base64

# For index Page / Landing Page / Home Page
def index(request):
    return render(request, 'index2.html')

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
    return render(request, 'restaurantlist.djt', context)

def restaurantProfile(request,slug):
    partnersappro = launchPartner.objects.filter(slug=slug).first()
    # uid= uuid.uuid4()
    # context = {"partnersappro": partnersappro, "uid":uid}
    # print("The uid is========= ",uid)
    if request.method == 'POST':
        amtt = request.POST["amount"]
        res = int(amtt)
        def genSha256(key, message):
            # partnersappro = launchPartner.objects.filter(slug=slug).first()
            key = key.encode('utf-8')
            message = message.encode('utf-8')

            hmac_sha256 = hmac.new(key, message, hashlib.sha256)
            digest = hmac_sha256.digest()

            # Convert the digest to a Base64-encoded string
            signature = base64.b64encode(digest).decode('utf-8')

            return signature

        # Example usage:
        
        total_amount = res
        secret_key = "8gBm/:&EnhH.1/q"
        uid= uuid.uuid4()
        data_to_sign = f"total_amount={total_amount},transaction_uuid={uid},product_code=EPAYTEST"

        result = genSha256(secret_key, data_to_sign)
        context = {
                "res":res,
                'total_amount': total_amount,
                "partnersappro": partnersappro,
                'uid': uid,
                'signature': result
        }
        return render(request, "foresewa.djt", context)
        # approvedPartners = launchPartner.objects.all()
        # print(approvedPartners)
        # context = {"approvedPartners": approvedPartners}
        # return render(request, 'fun.html', context)
    crustcontext= {"partnersappro": partnersappro}    
    return render(request, "restaurantProfile.djt", crustcontext)


def about(request):
    return render(request, 'about.djt')


def contactus(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cphone = request.POST['cphone']
        content = request.POST['content']
        contact = Contact(cname=cname,cemail=cemail, cphone=cphone, content=content)
        # print(contact)
        # messages.success(request, "Message Received!")
        contact.save()
        return render(request, 'contactus.djt', {'cname': cname})
    else:
        return render(request, 'contactus.djt', {})


# esewa function
# class VerifyEsewa(View):
#     def get(self, request):  
#         url ="https://uat.esewa.com.np/epay/transrec"
#         q= request.GET.get('q')
#         d = {
#             'amt': request.GET.get('amt'),
#             'scd': 'EPAYTEST',
#             'rid': request.GET.get('refid'),
#             # 'rid': '000AE01',
#             'pid':request.GET.get('oid'),
#         }
#         resp = req.post(url, d)
#         print("Status:========", resp.status_code)
#         # print(resp.text)
#         return HttpResponseRedirect(reverse('index'))