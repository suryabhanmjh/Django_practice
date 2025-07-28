from django.shortcuts import render, redirect
from .models import Student

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def registerdata(request):
    if request.method == 'POST':
        n = request.POST.get('fname')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        p = request.POST.get('password')
        cp = request.POST.get('cpassword')
        i = request.FILES.get('image')
        d = request.FILES.get('document')

        if Student.objects.filter(email=e).exists():
            msg = "Email already exists"
            return render(request, 'register.html', {'msg': msg})

        if p != cp:
            msg = "Password and Confirm Password do not match"
            return render(request, 'register.html', {'msg': msg})

        Student.objects.create(fname=n, email=e, contact=c, password=p, image=i, document=d)
        return redirect('login')

def logindata(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')

        try:
            user = Student.objects.get(email=e, password=p)
            return render(request, 'dashboard.html', {'user': user})
        except Student.DoesNotExist:
            msg = "Invalid email or password"
            return render(request, 'login.html', {'msg': msg})
