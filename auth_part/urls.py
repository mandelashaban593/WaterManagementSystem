from django.conf.urls import url
from . import views

app_name='auth_part'

urlpatterns = [
    url(r'^newuser/$', views.create_profile, name='createprofile'),
    url(r'^addwaterdata/$', views.addwaterdata, name='addwaterdata' ),
    # url(r'^editwaterdata/$', views.editwaterdata, name='editwaterdata' ),
    url(r'^search_waterdata/$', views.search_waterdata, name='search_waterdata' ),
    url(r'^search_result/$', views.search_result, name='search_result' ),
    url(r'^all_waterdata/$', views.all_waterdata, name='all_waterdata'),
    url(r'^all_waterdata/update/(?P<result_id>[0-9A-Za-z\.@\-\ ]+)/$', views.update_result, name='update'),
    url(r'^all_waterdata/delete/(?P<result_id>[0-9A-Za-z\.@\-\ ]+)/$', views.delete_result, name='delete'),
    url(r'^$', views.login, name='login'),
    url(r'^logout/', views.logout_view, name='logout'), #directly logging out by importing logout in view and using it here.   
]

