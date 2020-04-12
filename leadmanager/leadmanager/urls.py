
from django.contrib import admin
from django.urls import path, include
# 

urlpatterns = [
    path('', include('leads2.urls')),
    path('', include('accounts.urls'))
    
]
