from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth import login , logout , authenticate

# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        fm = RegistrationFrom(request.POST)
        if fm.is_valid:
            fm.save()
            return redirect('login')
    else:
        fm = RegistrationFrom()
    
    return render(request , 'register.html' , {'forms' : fm})

def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            print("Found user:", user_obj.username, "is_active:", user_obj.is_active)
            print("check_password:", user_obj.check_password(password))   # True/False
        except User.DoesNotExist:
            print("No user with this email")


        user = authenticate(request , username = user_obj.username , password = password)

        if user is not None:
            login(request , user)
            print("Login Successfull....")
            return redirect('dashboard')
            
        else:
            print("Login Failed")
            
            return redirect("register")

    return render(request , 'login.html')
