from django.urls import path
from . import views

app_name = 'likes'

urlpatterns=[
    path('like/',views.like,name='like'),
]
