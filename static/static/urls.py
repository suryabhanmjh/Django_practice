from django.contrib import admin
from django.urls import path
from app import views  # Import your views from the app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Assuming you have a home view in your app
]