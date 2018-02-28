from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restos import views

urlpatterns = [
    url(r'^restos/$', views.RestoList.as_view()),
    url(r'^restos/(?P<pk>[0-9]+)/$', views.RestoDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^register/$', views.Register.as_view()),
    url(r'^change_password/$', views.ChangePassword.as_view()),
    # url(r'^testing/$', views.index, name='index')
]

urlpatterns = format_suffix_patterns(urlpatterns)
