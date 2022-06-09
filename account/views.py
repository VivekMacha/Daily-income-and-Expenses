from django.shortcuts import redirect, render
from .models import UserInfo,UserForm,LoginForm
from income.models import Income
from expense.models import Expense
def get_balnace(request):
    uid=request.session.get('uid')  
    incl=Income.objects.filter(user=uid)
    expl=Expense.objects.filter(user=uid)
    total_income=0
    total_expense=0
    for i in incl:
        total_income=total_income+i.income
    for i in expl:
        total_expense=total_expense+i.expense

    return total_income-total_expense

def home(request):
    return render(request,'home.html',{'bal':get_balnace(request)})

def add_user(request):
    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f=UserForm
        context={'form':f}
        return render(request,'register.html',context)

from django.contrib.auth import authenticate,login,logout

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        passw=request.POST.get("password")
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return redirect("/")
        else:
            f=LoginForm
            context={'form':f,'lmsg':"Invalid UserName and Password ..."}
            return render(request,"login.html",context)    
    else:
        f=LoginForm
        context={'form':f}
        return render(request,"login.html",context)

def logout_view(request):
    logout(request)
    return redirect("/")

def edit_profile(request):
    uid=request.session.get('uid')  
    user=UserInfo.objects.get(id=uid)
    if request.method=='POST':
        f=UserForm(request.POST,instance=user)
        f.save()
        return redirect("/")
    else:
        f=UserForm(instance=user)
        context={'form':f}
        return render(request,'register.html',context)
