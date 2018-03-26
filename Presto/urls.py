from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'', include('restos.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)