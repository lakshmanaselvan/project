from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emanage/',include('django.contrib.auth.urls')),
    path('',include('emanage.urls')),
]
