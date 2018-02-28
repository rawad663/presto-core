from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
    url(r'', include('restos.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
    url(r'^login/', views.obtain_auth_token)
]
