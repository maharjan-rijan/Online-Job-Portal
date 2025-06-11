from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def aboutUs(request):
    return render(request, 'about-us.html')

def contactUs(request):
    return render(request, 'contact-us.html')