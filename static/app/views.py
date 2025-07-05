from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')  # Adjust the template path as needed