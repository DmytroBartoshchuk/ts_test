from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Carrier, Order, Trip


# main manager views
def index(request):
    return render(request, 'manager/index.html')


# carrier's views
class IndexCarrierView(generic.ListView):
    template_name = 'carriers/index.html'
    context_object_name = 'all_carriers'

    def get_queryset(self):
        return Carrier.objects.all()


class DetailCarrierView(generic.DetailView):
    model = Carrier
    template_name = 'carriers/detail.html'


# trip's views
class IndexTripView(generic.ListView):
    template_name = 'trips/index.html'
    context_object_name = 'all_trips'

    def get_queryset(self):
        return Trip.objects.all()


class DetailTripView(generic.DetailView):
    model = Trip
    template_name = 'trips/detail.html'


# order's views
class IndexOrderView(generic.ListView):
    template_name = 'orders/index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        return Order.objects.all()


class DetailOrderView(generic.DetailView):
    model = Order
    template_name = 'orders/detail.html'


# create, update, delete views
class CarrierCreate(CreateView):
    model = Carrier
    fields = ['name', 'register_date']
    template_name = 'carriers/carrier_form.html'


class CarrierUpdate(UpdateView):
    model = Carrier
    fields = ['name', 'register_date']
    template_name = 'carriers/carrier_form.html'


class CarrierDelete(DeleteView):
    model = Carrier
    success_url = reverse_lazy('manager:carrier_list')