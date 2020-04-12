from django.contrib import admin
from django.urls import path

from config import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
]
