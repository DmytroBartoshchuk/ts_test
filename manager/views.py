from django.shortcuts import render, get_object_or_404
from .models import Carrier, Order, Trip


def index(request):
    return render(request, 'manager/index.html')


def carrier_list(request):
    all_carriers = Carrier.objects.all()
    context = {'all_carriers': all_carriers}
    return render(request, 'carriers/index.html', context)


def carrier_detail(request, carrier_id):
    carrier = get_object_or_404(Carrier, pk=carrier_id)
    return render(request, 'carriers/detail.html', {'carrier': carrier})


def trip_list(request):
    all_trips = Trip.objects.all()
    context = {'all_trips': all_trips}
    return render(request, 'trips/index.html', context)


def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'trips/detail.html', {'trip': trip})


def order_list(request):
    all_orders = Order.objects.all()
    context = {'all_orders': all_orders}
    return render(request, 'orders/index.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/detail.html', {'order': order})