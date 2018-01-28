from django.shortcuts import render


def welcome(request):
    return render(request, 'manager/welcome.html')