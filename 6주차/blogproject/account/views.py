from django.contrib import auth
from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm

def login_view(request):
    if request.method=='POST':
        form =AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            #form에서받은 data들 username,password를 가지고 인증받음
            user=authenticate(request=request,username=username,password=password)
            if user is not None:
                login(request,user)                
        return redirect("home")
        
    else: #method==GET
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)        
        return redirect("home")
    else:        
        form=RegisterForm()
        return render(request,'signup.html',{'form':form})

