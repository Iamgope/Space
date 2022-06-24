from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.frontPage ,name='frontPage'),
    path('signUp/',views.SignUp,name="SignUp"),
    path('login/',auth_views.LoginView.as_view(template_name="core/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view())

]