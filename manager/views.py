from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Carrier, Order, Trip


def index(request):
    return render(request, 'manager/index.html')


def carrier_list(request):
    all_carriers = Carrier.objects.all()
    context = {'all_carriers': all_carriers}
    return render(request, 'carriers/index.html', context)


def carrier_detail(request, carrier_id):
    try:
        carrier = Carrier.objects.get(pk=carrier_id)
    except Carrier.DoesNotExist:
        raise Http404("Carrier does not exist")
    return render(request, 'carriers/detail.html', {'carrier': carrier})


def trip_list(request):
    all_trips = Trip.objects.all()
    context = {'all_trips': all_trips}
    return render(request, 'trips/index.html', context)


def trip_detail(request, trip_id):
    try:
        trip = Trip.objects.get(pk=trip_id)
    except Trip.DoesNotExist:
        raise Http404("Trip does not exist")
    return render(request, 'trips/detail.html', {'trip': trip})


def order_list(request):
    all_orders = Order.objects.all()
    context = {'all_orders': all_orders}
    return render(request, 'orders/index.html', context)


def order_detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404("Trip does not exist")
    return render(request, 'orders/detail.html', {'order': order})