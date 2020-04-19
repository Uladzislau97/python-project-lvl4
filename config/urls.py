from django.contrib import admin
from django.urls import path, include

from config import views

urlpatterns = [
    path('', views.index),
    path('', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),
    path('admin/', admin.site.urls),
]
