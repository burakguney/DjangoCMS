from django.shortcuts import render
from django.http import HttpRequest
from .models import Career
# Create your views here.


def careerList_en(request):
    careerList = Career.objects.all()
    return render(request, 'en/career/careerList.html', {"careerList": careerList})


def careerSingle_en(request, careerSlug, pk):
    careerSingle = Career.objects.get(pk=pk)
    return render(request, 'en/career/careerSingle.html', {"careerSingle": careerSingle})
