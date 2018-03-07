from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restos import views

urlpatterns = [
    url(r'^restos/$', views.RestoList.as_view()),
    url(r'^restos/([0-9]+)/$', views.RestoDetail.as_view()),
    url(r'^users/([0-9]+)/$', views.UserDetail.as_view()),
    #url('accounts/', include('django.contrib.auth.urls')),
    #url('accounts/register/', views.Register.as_view(), name='register'), 
    url('register/customer/', views.RegisterCustomer.as_view(), name='customer_register'),
    url('register/resto/', views.RegisterResto.as_view(), name='resto_register'),
    #url('change_password/', views.ChangePassword.as_view()),
    # url(r'^testing/$', views.index, name='index')
]
