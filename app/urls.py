from django.urls import path
from . import views

urlpatterns = [
    path('base_layout/',views.base_layout,name="base_layout"),
    path('about/',views.about),
]
