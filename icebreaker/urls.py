from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('register/',include('register.urls')),
    path('comment/',include('comment.urls')),
    path('likes/',include('likes.urls')),
]
