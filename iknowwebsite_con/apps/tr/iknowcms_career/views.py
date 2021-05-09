from django.shortcuts import render
from django.http import HttpRequest
from .models import Career
# Create your views here.


def careerList(request):
    careerList = Career.objects.all()
    return render(request, 'tr/career/careerList.html', {"careerList": careerList})


def careerSingle(request, careerSlug, pk):
    careerSingle = Career.objects.get(pk=pk)
    return render(request, 'tr/career/careerSingle.html', {"careerSingle": careerSingle})
