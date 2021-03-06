from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from django.urls import path

app_name = 'startFundraiser'

urlpatterns = [
    # /startFundraiser/
    path('', views.home, name='home'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login_user/$', views.login_user, name='login_user'),
    #url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^start_campaign/$', views.start_campaign, name='start_campaign'),
    path('edit/<int:pk>', views.campaign_edit, name='campaign_edit'),
    path('delete/<int:pk>', views.campaign_delete, name='campaign_delete'),
    # url(r'^all_campaigns/$', views.IndexView.as_view(), name='campaigns'),
    url(r'^all_campaigns/$', views.campaigns, name='campaigns'),
    url(r'^campaigns/creative/$', views.creative, name='creative'),
    url(r'^campaigns/social/$', views.social, name='social'),
    url(r'^campaigns/tech/$', views.tech, name='tech'),
    url(r'^campaign/(?P<campaign_id>[0-9]+)/$', views.detail, name='campaign_detail'),
    url(r'^campaign/(?P<pk>\d+)/update/$', views.add_update, name='add_update'),
    url(r'^campaign/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^campaign/(?P<pk>\d+)/faq/$', views.add_faq, name='add_faq'),
    url(r'^index/$', views.index, name='index'),
    url(r'^posts/$', views.blog_post, name='blog_post'),
    url(r'^campaign/(?P<pk>\d+)/support/$', views.campaign_support, name='campaign_support'),
    url(r'^campaign/(?P<pk>\d+)/pay/$', views.pay, name='pay'),
    url(r'^checkout/(?P<pk>\d+)/$', views.checkout, name='checkout'),
    #path('update-transaction/<int:pk>/', views.update_transaction_records,name='update_records'),
    #url(r'^update-transaction/(?P<token>[-\w]+)/$', views.update_transaction_records,name='update_records'),
    url(r'^update-transaction/(?P<pk>\d+)/$', views.update_transaction_records,name='update_records'),
    url(r'^like/$', views.like_camp, name='like_camp'),

]
