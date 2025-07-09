from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
def landing(req):
    return render(req, 'landing.html')
def register(req):
    return render(req, 'landing.html', {'register':'register'})
def registerdata(req):
    if req.method=='POST':
       n=req.POST.get('fname')
       e=req.POST.get('email')
       i=req.POST.get('image')
       c=req.POST.get('contact')
       d=req.POST.get('document')
       print(n, e, i, c, d, sep=',') 
       Student.objects.create(fname=n, email=e, contact=c, image=i, document=d)
       return HttpResponse("registration done")