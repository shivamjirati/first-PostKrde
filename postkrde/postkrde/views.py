from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")