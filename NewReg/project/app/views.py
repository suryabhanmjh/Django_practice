from django.shortcuts import render,redirect
from .models import Student, Query
from django.urls import reverse
from urllib.parse import urlencode 

# Create your views here.
def home(req):
    return render(req,'home.html')

def register(req):
    if req.method == 'POST':
        n = req.POST.get('fname')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        i = req.FILES.get('image')
        d = req.FILES.get('document')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')
        # print(n,e,c,i,d,p,cp)
        user = Student.objects.filter(email=e)
        if user:
            msg = "Email already exist"
            return render(req,'register.html',{'msg':msg})   
        else:
            if p==cp:
                data = {
                    'fname':n,'email':e,'contact':c,'image':i,'document':d,'password':p
                }
                Student.objects.create(fname=n,email=e,contact=c,image=i,document=d,password=p)
                return redirect('login')
            else:
                pmsg = "Password and Conform password not match"
                return render(req,'register.html',{'pmsg':pmsg})
    return render(req,'register.html')   

def login(req):
    if req.method == "POST":
        e = req.POST.get("email")
        p = req.POST.get("password")
        
        user = Student.objects.filter(email=e)
        if user:
            data = Student.objects.get(email=e)
            upass = data.password
            if upass == p:
                # url = reverse('dashboard')
                # data = urlencode({'id': data.id})
                # return redirect(f'{url}?{data}')
                req.session['id'] = data.id
                url = reverse('dashboard')
                return redirect(f'{url}')
            else:
                msg = "Email and password not match"
                return render(req, 'login.html',{'pmsg':msg,'email':e})
        else:
            return redirect('register')
    return render(req,'login.html')

def dashboard(req):
    # pk = req.GET.get('id')
    pk = req.session['id']
    if not pk:
        return redirect('login')
    
    try:
        user = Student.objects.get(id=pk)
        data = {
            'fname': user.fname,
            'email': user.email,
            'contact': user.contact,
            'image': user.image,
            'document': user.document,
            'password': user.password
        }
        return render(req, 'dashboard.html', {'data': data})
    except Student.DoesNotExist:
        return redirect('login')
    
def logout(req):
    req.session.flush()
    return redirect('home')   

def query(req):
    data = req.session.get('id', None)
    if data:
        pk = req.session['id']
        user = Student.objects.get(id=pk)
        data = {'fname': user.fname, 'email': user.email, 'contact': user.contact, 
                'image': user.image, 'document': user.document, 'password': user.password}
        return render(req, 'dashboard.html', {'data': data, 'query':'query'})
    else:
        return redirect('login')
    
def querydata(req):
    if req.method == 'POST':
        n = req.POST.get('fname')
        e = req.POST.get('email')
        q = req.POST.get('query')  
        
        Query.objects.create(name=n, email=e, message=q)
        
        # Get user data for dashboard
        pk = req.session['id']
        user = Student.objects.get(id=pk)
        data = {
            'fname': user.fname,
            'email': user.email,
            'contact': user.contact,
            'image': user.image,
            'document': user.document,
            'password': user.password
        }
        
        # Add success message
        success_msg = "Your query has been submitted successfully!"
        return render(req, 'dashboard.html', {'data':data, 'success_msg': success_msg})
    
    # If not POST request, redirect to dashboard
    return redirect('dashboard')
