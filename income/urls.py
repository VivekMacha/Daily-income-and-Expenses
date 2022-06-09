from django.urls import path
from .import views as v
urlpatterns = [
    path('add',v.add_income,name="add"),
    path('list',v.income_list,name="list"),
    path('delete/<int:id>',v.delete_income,name="delete"),
    path('serch-income-type/<str:data>',v.search_by_incometype,name="search_type"),
]
