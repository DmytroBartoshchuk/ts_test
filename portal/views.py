from django.shortcuts import render
from manager.models import Carrier, Order, Trip


def index(request):
    return render(request, 'portal/index.html')


def results(request):
    return render(request, 'portal/results.html')
