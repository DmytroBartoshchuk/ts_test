from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from manager import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^manager/', include('manager.urls')),
    url(r'^portal/', include('portal.urls')),
    url(r'^serialized/', views.TripList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)