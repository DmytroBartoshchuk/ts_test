from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^manager/', include('manager.urls')),
    url(r'^portal/', include('portal.urls')),
]
