from django.contrib import admin
from django.urls import path, include

from config import views

urlpatterns = [
    path('', views.index),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
