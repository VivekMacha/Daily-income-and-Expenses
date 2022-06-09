from django.shortcuts import render,redirect
from .models import Expense,ExpenseForm,User
def add_expense(request):
    if request.method=='POST':
        f=ExpenseForm(request.POST)    
        f.save()
        exp=Expense()
        uid=request.session.get("uid")
        user=User.objects.get(id=uid)
        exp.user=user
        
        return redirect("/")
    else:
        f=ExpenseForm
        context={'form':f}
        return render(request,'addexpense.html',context)
