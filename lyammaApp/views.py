from django.shortcuts import render

# Create your views here.

#For index Page / Landing Page / Home Page
def index(request):
    return render(request, 'base.html')