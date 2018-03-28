# from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^restos/$', views.RestoList.as_view(), name='resto_list'),
    url(r'^restos/([0-9]+)/$', views.RestoDetail.as_view(), name='resto_detail'),
    url(r'^customers/$', views.CustomerList.as_view()),
    url(r'^customers/([0-9]+)/$', views.CustomerDetail.as_view(), name='customer_detail'),
    url('login-main/', views.CustomObtainAuthToken.as_view(), name='login'),
    url('register/customer/', views.RegisterCustomer.as_view(), name='register_customer'),
    url('register/resto/', views.RegisterResto.as_view(), name='register_resto'),
    url('like-resto/([0-9]+)/', views.LikeResto.as_view(), name='like_resto'),
    url('dislike-resto/([0-9]+)/', views.DislikeResto.as_view(),name='dislike_resto'),
    url('reserve/([0-9]+)/([0-9]+)/', views.MakeReservation.as_view(), name='reserve'),
    url(r'^reservations/', views.Reservations.as_view(), name='reservation'),
    url(r'^reservations/([0-9]+)/', views.ReserveDetail.as_view(), name='reservation_detail'),
    url(r'^reservations/([0-9]+)/accept/', views.AcceptReservation.as_view(), name='accept_reservation'),
    url(r'^reservations/([0-9]+)/decline/', views.DeclineReservation.as_view()),
]
