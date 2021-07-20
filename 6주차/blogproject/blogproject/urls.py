
from django.contrib import admin
from django.urls import path,include
from blogapp.views import home

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('blogapp/',include('blogapp.urls')),
    path('accont/',include('account.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    #↑복붙해서 쓰면댐