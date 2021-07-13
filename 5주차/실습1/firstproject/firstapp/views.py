from django.shortcuts import render

def welcome(request):
    return render(request,"welcome.html")

def hello(request):
    userName=request.GET['name'] #welcome에서 name 전달받기
    return render(request,'hello.html',{'userName':userName}) 
    #userName hello.html로 보내주기

