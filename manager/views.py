from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Carrier, Order, Trip
from .forms import UserForm
from .serializers import TripSerializer
from .utils import render_to_pdf


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


# registration view
class UserFormView(View):
    form_class = UserForm
    template_name = 'manager/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('manager:index')

        return render(request, self.template_name, {'form': form})


# JSON view (Lists all trips or create a new one)
# serialized/
class TripList(APIView):

    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# pdf view
# /ticket_pdf/
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/ticket.html')
        #template_name = 'pdf/ticket.html'
        context = {
            'id': 123,
            'carrier': 'Trans',
            'name': 'Dima',
            'surname': 'Bart',
            'email': 'ad@ad.com',
            'phone': '20000025252'
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/ticket.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'Ticket_number_%s.pdf' % "1235131"
            content = "inline; filename='%s'" % filename
            # if param download has some value - automatic downloading
            download = request.GET.get('download')
            if download:
                content = "attachment; filename='%s'" % filename
            response['Content-Disposition'] = content
            return response
        return HttpResponse('PDF file not found')














