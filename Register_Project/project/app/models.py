from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/')
    document = models.FileField(upload_to='student_docs/')

    def __str__(self):
        return self.fname
