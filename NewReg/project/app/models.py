from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    password=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image/')
    document=models.FileField(upload_to='file/')

    def __str__(self):
        return self.fname

class Query(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
