from os import name
from django.urls import path
from .import views as v
urlpatterns = [
    path('register',v.add_user,name="add"),
    path('login',v.login_view,name="login"),
    path('logout',v.logout_view,name="logout"),
    path('update',v.edit_profile,name="profile")
]
