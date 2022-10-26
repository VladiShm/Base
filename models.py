from django.db import models

class Person(models.Model):
    FirstName = models.CharField(max_length=100)
    SecondName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Departament = models.CharField(max_length=100)

class Authorization(models.Model):
    Login = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Success = models.BooleanField(default = False)


