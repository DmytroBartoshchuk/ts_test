from django.conf.urls import url
from . import views

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

    #
    url(r'carrier/add/$', views.CarrierCreate.as_view(), name='carrier-add'),
]
