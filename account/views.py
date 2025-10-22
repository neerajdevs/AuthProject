from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth import login , logout , authenticate
from django.db import transaction

# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        fm = RegistrationFrom(request.POST)
        if fm.is_valid():
            with transaction.atomic():
                # form se instance banao but abhi save mat karo
                user = fm.save(commit=False)
                # password ko hash karo
                user.set_password(fm.cleaned_data['password1'])
                # ab DB me save karo
                user.save()

                # agar profile create karni ho:
                Profile.objects.get_or_create(user=user)
                login(request , user)
                return redirect('home')
    else:
        fm = RegistrationFrom()
    
    return render(request , 'register.html' , {'forms' : fm})

def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        user_obj = User.objects.get(email=email)
        user = authenticate(request , username = user_obj.username , password = password)

        if user is not None:
            login(request , user)
            print("Login Successfull....")
            return redirect('dashboard')
            
        else:
            print("Login Failed")
            
            return redirect("register")

    return render(request , 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')