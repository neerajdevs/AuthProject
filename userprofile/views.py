from django.shortcuts import render,redirect
from account.forms import *
from account.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def HomeView(request):
    return render(request , "home.html")


@login_required
def DashboardView(request):
    return render(request , 'dashboard.html')

@login_required
def ProfileView(request):
    profilefm = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profilefm)
    return render(request , 'profile.html' , {"form" : form})


@login_required
def EditView(request):
    profile = Profile.objects.get(user=request.user)  # current user ka profile fetch

    if request.method == 'POST':
        editfm = ProfileForm(request.POST, request.FILES, instance=profile)
        if editfm.is_valid():
            editfm.save()
            print("Profile Updated Successfully ✅")
            return redirect('profile')  # apni profile page ka url name daal yahan
        else:
            print(editfm.errors)
    else:
        editfm = ProfileForm(instance=profile)

    return render(request, 'edit-profile.html', {'form': editfm})