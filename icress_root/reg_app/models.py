from django.db import models

# Create your models here.

class Student(models.Model):
    firstname= models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    contactNumber=models.IntegerField()
    emailId=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    python=models.CharField(max_length=100)
    django=models.CharField(max_length=100)
    java=models.CharField(max_length=100)
    bigdata=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confomepassword=models.CharField(max_length=100)




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)
    def __str__(self):
        return self.name