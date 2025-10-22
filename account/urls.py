from django.urls import path , include
from .views import *
urlpatterns = [
    path("auth/register" , RegisterView , name='register'),
    path("auth/login" , LoginView , name='login'),
    path("auth/logout" , logout_view , name='logout'),
]
