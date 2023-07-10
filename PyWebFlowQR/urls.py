from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('transactions', include('home.urls')),
    path('qr', include('home.urls')),
]
