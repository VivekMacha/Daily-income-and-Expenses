from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    expense=models.IntegerField()
    expense_type=models.CharField(max_length=30)
    expense_date=models.DateField(auto_now=True)
    description=models.TextField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table="expense"

from django import forms

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields=["id","expense",'expense_type','description','user']