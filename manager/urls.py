from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'manager'

urlpatterns = [
    # /manager/
    url(r'^$', views.index, name='index'),

    # /manager/carriers/
    url(r'^carriers/$', views.IndexCarrierView.as_view(), name='carrier_list'),

    # /manager/carriers/<carrier_id>/
    url(r'^carriers/(?P<pk>[0-9]+)/$', views.DetailCarrierView.as_view(), name='carrier_detail'),

    # /manager/orders/
    url(r'^orders/$', views.IndexOrderView.as_view(), name='order_list'),

    # /manager/orders/<order_id>/
    url(r'^orders/(?P<pk>[0-9]+)/$', views.DetailOrderView.as_view(), name='order_detail'),

    # /manager/trips/
    url(r'^trips/$', views.IndexTripView.as_view(), name='trip_list'),

    # /manager/trip/<trip_id>/
    url(r'^trips/(?P<pk>[0-9]+)/$', views.DetailTripView.as_view(), name='trip_detail'),

    # /manager/carrier/add/
    url(r'^carrier/add/$', views.CarrierCreate.as_view(), name='carrier-add'),

    # /manager/carrier/<carrier_id>/
    url(r'^carrier/(?P<pk>[0-9]+)/$', views.CarrierUpdate.as_view(), name='carrier-update'),

    # /manager/carrier/<carrier_id>/delete/
    url(r'^carrier/(?P<pk>[0-9]+)/delete/$', views.CarrierDelete.as_view(), name='carrier-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)