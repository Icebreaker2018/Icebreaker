"""iceBreaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import settings
from . import views
from django.conf.urls.static import static
from startFundraiser import views as blog_views
from django.urls import path, include, re_path
#from django.contrib.auth.views import (password_reset, password_reset_done,
#                                    password_reset_confirm,password_reset_complete)
from django.contrib.auth import views as auth_views
from marketplace import views as marketplace_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('register/', include('register.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('startfundraiser/', include('startFundraiser.urls')),
    path('community/', include('community.urls')),
    path('polls/', include('polls.urls')),
    path('testimony/', include('testimony.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'add/post/', blog_views.add_post, name='add_post'),
    url(r'^edit/post/(?P<id>\d+)/$', blog_views.edit_post, name='edit_post'),
    url(r'del/post/(?P<id>\d+)/$', blog_views.del_post, name='del_post'),
    #url(r'api/products/',marketplace_views.productsListView.as_view()),
    url(r'api/funds/',blog_views.fundsListView.as_view()),
    url(r'^messenger/$',views.message, name="messenger"),
    path('',include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
