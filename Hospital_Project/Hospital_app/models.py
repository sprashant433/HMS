from django.db import models


# Create your models here.


class Userinfo(models.Model):
    objects = models.Manager()
    uniqueID = models.CharField(max_length=246, unique=True)
    Username = models.CharField(max_length=128)
    Email = models.EmailField(max_length=246, unique=True)
    First_Name = models.CharField(max_length=128)
    Last_Name = models.CharField(max_length=128)
    DOB = models.DateField()
    Password = models.CharField(max_length=128)

    def __str__(self):
        return self.Email
