"""Presto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
<<<<<<< HEAD
from rest_framework.urlpatterns import format_suffix_patterns
=======
from rest_framework.authtoken import views
>>>>>>> 2d88a7a2ac71fd6a8a367ae7b10deb2950ada76b

urlpatterns = [
    url(r'', include('restos.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
<<<<<<< HEAD
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
=======
    url(r'^login/', views.obtain_auth_token)
]
>>>>>>> 2d88a7a2ac71fd6a8a367ae7b10deb2950ada76b
