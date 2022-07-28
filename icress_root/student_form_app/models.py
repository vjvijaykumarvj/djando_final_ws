from django.db import models

# Create your models here.
class StudentDjangoForms(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    ContactNumber=models.IntegerField()
    Emailid=models.EmailField(max_length=100)
    Address=models.CharField(max_length=100)
    Confirm_Emailid=models.CharField(max_length=100)
    Date_of_Birth=models.DateField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Python=models.CharField(max_length=100)
    Java=models.CharField(max_length=100)