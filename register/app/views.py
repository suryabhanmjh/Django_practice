from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
def landing(req):
    return render(req, 'landing.html')
def register(req):
    return render(req, 'register.html')
def login(req):
    return render(req, 'login.html')
def registerdata(req):
    if req.method=='POST':
       n=req.POST.get('fname')
       e=req.POST.get('email')
       i=req.FILES.get('image')
       c=req.POST.get('contact')
       p=req.POST.get('password')
       cp=req.POST.get('cpassword')
       d=req.FILES.get('document')

       data =Student.objects.filter(email=e)
       if data:
            msg = "Email already exists"
            return render(req, 'landing.html', {'msg': msg, 'register':'register'})
       else:
            if p==cp:
                Student.objects.create(fname=n, email=e, contact=c, image=i, document=d, password=p)
                msg='Registration done'
                return render(req, 'landing.html', {'login':'login'})
            else:
                msg = "Password and confirm password do not match"
                return render(req, 'landing.html', {'pmsg': msg, 'register':'register'})
       
       print(n, e, i, c, d, ) 
    #    Student.objects.create(fname=n, email=e, contact=c, image=i, document=d, password=p, cpassword=cp)
    #    return HttpResponse("registration done")