
from django.urls import path
from .views import *

#blog 앱에있는 views의 문법 다 가져오기
urlpatterns = [        
    path('detail/<str:id>',detail,name="detail"),
    path('new/',new,name="new"),
    path('create/',create,name="create"),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>',update,name="update"),
    path('delete/<str:id>',delete,name="delete"),    
    
]