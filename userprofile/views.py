from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request , "home.html")

def DashboardView(request):
    return render(request , 'dashboard.html')