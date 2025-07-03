from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request, 'app/demo.html', { 'name': 'suryabhan singh', 'data': ['python', 'django', 'flask', 'java'] })