import imp
from django.db import models
from django.contrib.auth.models import User
class Income(models.Model):
    income=models.IntegerField()
    income_type=models.CharField(max_length=30)
    incom_date=models.DateField(auto_now=True)
    description=models.TextField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table="income"

from django import forms

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields='__all__'