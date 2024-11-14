from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from  django.contrib.auth import login,logout

from django.contrib import messages

def signup_page(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'You have been successfully signup!!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'singup.html',{'form':form})

def signin_page(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,'Successfully you are loggedIn')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'signin.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'Successfully you are LoggedOut')
    return redirect('signin')