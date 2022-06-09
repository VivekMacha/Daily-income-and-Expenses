from datetime import date
from django.shortcuts import redirect, render
from .models import Income,IncomeForm,User

def add_income(request):
    if request.method=='POST':
        inc=Income()
        income=request.POST.get("income")
        income_type=request.POST.get("income_type")
         
        description=request.POST.get("description")
        inc.income=income
        
        inc.income_type=income_type
        inc.description=description
        uid=request.session.get("uid")
        usr=User.objects.get(id=uid)
        inc.user=usr
        inc.save()
        return redirect("/")
    else:
        f=IncomeForm
        context={'form':f}
        return render(request,'addincome.html',context)


def income_list(request):
  uid=request.session.get("uid")
  usr=User.objects.get(id=uid)
  incl=Income.objects.filter(user=usr)
  inctype=set()
  for i in incl:
    inctype.add(i.income_type)
  if request.method=='POST':
    srch=request.POST.get("search")
    inclist=Income.objects.filter(user=usr,description__contains=srch)
    return render(request,'incomelist.html',{'incl':inclist,'inctype':inctype})  
  else:
    return render(request,'incomelist.html',{'incl':incl,'inctype':inctype})  

def search_by_incometype(request,data):
  uid=request.session.get("uid")
  usr=User.objects.get(id=uid)
  incl=Income.objects.filter(user=usr)
  inctype=set()
  for i in incl:
    inctype.add(i.income_type)
  inclist=Income.objects.filter(user=usr,income_type=data)
  return render(request,"incomelist.html",{'incl':inclist,'inctype':inctype})

def delete_income(request,id):
  inc=Income.objects.get(id=id)
  inc.delete()
  return redirect("/")
  