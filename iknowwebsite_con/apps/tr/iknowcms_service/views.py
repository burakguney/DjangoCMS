from django.shortcuts import render
from django.http import HttpRequest
from .models import Service
# Create your views here.


def serviceList(request):
    serviceList = Service.objects.all()
    return render(request, 'tr/service/serviceList.html', {"serviceList": serviceList})


def serviceSingle(request, serviceSlug):
    serviceSingle = Service.objects.get(serviceSlug=serviceSlug)
    return render(request, 'tr/service/serviceSingle.html', {"serviceSingle": serviceSingle})


def servicePartial(request):
    servicePartial = Service.objects.all()
    return render(request, 'tr/service/servicePartial.html', {"servicePartial": servicePartial})
