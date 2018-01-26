from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from manager import views
from ticksell import views as main_views

urlpatterns = [
    url(r'^$', main_views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^manager/', include('manager.urls')),
    url(r'^portal/', include('portal.urls')),
    url(r'^serialized/', views.TripList.as_view()),
    url(r'^ticket_pdf/', views.GeneratePDF.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)