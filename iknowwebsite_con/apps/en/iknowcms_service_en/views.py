from django.shortcuts import render
from django.http import HttpRequest
from .models import Service
# Create your views here.


def serviceList_en(request):
    serviceList = Service.objects.all()
    return render(request, 'en/service/serviceList.html', {"serviceList": serviceList})


def serviceSingle_en(request, serviceSlug):
    serviceSingle = Service.objects.get(serviceSlug=serviceSlug)
    return render(request, 'en/service/serviceSingle.html', {"serviceSingle": serviceSingle})


def servicePartial_en(request):
    servicePartial = Service.objects.all()
    return render(request, 'en/service/servicePartial.html', {"servicePartial": servicePartial})
