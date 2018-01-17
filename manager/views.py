from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Carrier, Order, Trip


def index(request):
    return render(request, 'manager/index.html')


'''
def carrier_list(request):
    all_carriers = Carrier.objects.all()
    context = {'all_carriers': all_carriers}
    return render(request, 'carriers/index.html', context)


def carrier_detail(request, carrier_id):
    carrier = get_object_or_404(Carrier, pk=carrier_id)
    return render(request, 'carriers/detail.html', {'carrier': carrier})
'''


class IndexCarrierView(generic.ListView):
    template_name = 'carriers/index.html'
    context_object_name = 'all_carriers'

    def get_queryset(self):
        return Carrier.objects.all()


class DetailCarrierView(generic.DetailView):
    model = Carrier
    template_name = 'carriers/detail.html'


'''
def trip_list(request):
    all_trips = Trip.objects.all()
    context = {'all_trips': all_trips}
    return render(request, 'trips/index.html', context)


def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'trips/detail.html', {'trip': trip})
'''


class IndexTripView(generic.ListView):
    template_name = 'trips/index.html'
    context_object_name = 'all_trips'

    def get_queryset(self):
        return Trip.objects.all()


class DetailTripView(generic.DetailView):
    model = Trip
    template_name = 'trips/detail.html'


'''
def order_list(request):
    all_orders = Order.objects.all()
    context = {'all_orders': all_orders}
    return render(request, 'orders/index.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/detail.html', {'order': order})
'''


class IndexOrderView(generic.ListView):
    template_name = 'orders/index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        return Order.objects.all()


class DetailOrderView(generic.DetailView):
    model = Order
    template_name = 'orders/detail.html'


class CarrierCreate(CreateView):
    model = Carrier
    fields = ['name', 'register_date']
