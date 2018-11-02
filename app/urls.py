from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('base_layout/',views.base_layout,name="base_layout"),
    path('about/',views.about,name="about"),
]
