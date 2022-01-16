from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class Hospital(models.Model):
    title=models.CharField(max_length=40)

    def __str__(self) :
        return self.title

class Company(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self) :
        return self.title

class people(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    national_code=models.CharField(max_length=10,unique=True,error_messages={
            'unique': ("A user with that national code already exists."),
        },)
    hospital=models.ForeignKey(Hospital,on_delete=models.DO_NOTHING,related_name="users")
    company=models.ForeignKey(Company,on_delete=models.DO_NOTHING,related_name="workers")
    covid_test=models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.national_code


# class user(User):
#     email = models.EmailField(blank=True,null=True)
#     national_code=models.CharField(max_length=10,unique=True,error_messages={
#             'unique': ("A user with that national code already exists."),
#         },)
#     hospital=models.ForeignKey(Hospital,on_delete=models.DO_NOTHING,related_name="users")
#     company=models.ForeignKey(Company,on_delete=models.DO_NOTHING,related_name="workers")
#     covid_test=models.BooleanField(default=False)
#     phone_number = models.CharField(max_length=11, verbose_name="phone number")

#     REQUIRED_FIELDS = ['national_code']

   
#     def __str__(self):
#         return self.national_code



