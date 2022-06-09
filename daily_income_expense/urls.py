from django.contrib import admin
from django.urls import path,include
from account.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('acc-',include(("account.urls",'account'),namespace="account")),
    path('income-',include(("income.urls",'income'),namespace="income")),
    path('expense-',include(("expense.urls",'expense'),namespace="expense")),
]
