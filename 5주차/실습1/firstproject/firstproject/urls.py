"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views as first
from secondapp import views as second
#views 중복 금지
#해결법1) import firstapp.views:from을 쓰지않고, 
#해결법2) from wordcount import views as first : first.hello

urlpatterns = [
    #URL주소 겹치면 안됌!
    path('admin/', admin.site.urls), #URL + /admin/-> admin.site.urls가 실행됨
    path('',first.welcome,name="welcome"), #URL+' '-> welcome 실행
    #다른html에서 URL 대신에 name을 사용한다
    path('hello/',first.hello,name="hello"),
    path('wc/',second.wordcount,name="wordcount"),
    path('wc/result/',second.result,name="result"),
]
