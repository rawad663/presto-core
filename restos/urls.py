from django.conf.urls import url
from restos import views
from rest_framework.authtoken import views as authViews

urlpatterns = [
    url(r'^restos/$', views.RestoList.as_view()),
    url(r'^restos/([0-9]+)/$', views.RestoDetail.as_view()),
    url(r'^customers/([0-9]+)/$', views.CustomerDetail.as_view()),
    url('register/customer/', views.RegisterCustomer.as_view()),
    url('register/resto/', views.RegisterResto.as_view()),
    url('like-resto/([0-9]+)/', views.LikeResto.as_view()),
    url('reserve/([0-9]+)/([0-9]+)/', views.Reserve.as_view()),
    url('reservations/', views.Reservations.as_view()),
    url('reserve/([0-9]+)/delete/', views.delete_reserve),

]
