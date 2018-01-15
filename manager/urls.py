from django.conf.urls import url
from . import views

urlpatterns = [
    # /manager/
    url(r'^$', views.index, name='index'),

    # /manager/carriers/
    url(r'^carriers/$', views.carrier_list, name='carrier_list'),

    # /manager/carriers/?/
    url(r'^carriers/(?P<carrier_id>[0-9]+)/$', views.carrier_detail, name='carrier_detail'),

    # /manager/orders/
    url(r'^orders/$', views.order_list, name='order_list'),

    # /manager/orders/?/
    url(r'^orders/(?P<order_id>[0-9]+)/$', views.order_detail, name='order_detail'),

    # /manager/trips/
    url(r'^trips/$', views.trip_list, name='trip_list'),

    # /manager/trip/?/
    url(r'^trips/(?P<trip_id>[0-9]+)/$', views.trip_detail, name='trip_detail'),
]
