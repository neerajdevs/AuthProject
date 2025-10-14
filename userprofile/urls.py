from .views import *
from django.urls import path

urlpatterns = [
  path("" , HomeView , name = "home"),
  path('dashboard/' , DashboardView , name='dashboard'),
  path('profile' , ProfileView , name = 'profile'),
  path('profile/edit' , EditView , name = 'edit-profile'),
]
