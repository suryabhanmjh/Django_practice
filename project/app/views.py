from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'app/landing.html',)
def home(request):
    return render(request,'app/home.html')
def about(request):
    return render(request,'app/about.html')
def contact(request):
    return render(request,'app/contact.html')
def services(request):
    return render(request,'app/services.html')
def registration(request):
    return render(request,'app/registration.html')
def login(request):
    return render(request,'app/login.html')