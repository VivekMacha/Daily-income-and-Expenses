import imp
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserInfo(User):
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=15)
    address=models.TextField(max_length=300)
    class Meta:
        db_table="user_info"



class UserForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','age','email','contact','gender','address','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)
