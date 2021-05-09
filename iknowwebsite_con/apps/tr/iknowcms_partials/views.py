from django.shortcuts import render
from django.http import HttpRequest
from .models import Testimonial, Client, Carousel
from apps.tr.iknowcms_pages.models import Contact

# Create your views here.


def carouselPartial(request):
    carouselPartial = Carousel.objects.all()
    return render(request, 'tr/partials/home/carouselPartial.html', {"carouselPartial": carouselPartial})


def carouselSingle(request, carouselSlug):
    carouselSingle = Carousel.objects.get(carouselSlug=carouselSlug)
    return render(request, 'tr/partials/home/carouselSingle.html', {"carouselSingle": carouselSingle})


def testimonialPartial(request):
    testimonialPartial = Testimonial.objects.all()
    return render(request, 'tr/partials/home/testimonialPartial.html', {"testimonialPartial": testimonialPartial})


def clientPartial(request):
    clientPartial = Client.objects.all()
    return render(request, 'tr/partials/home/clientPartial.html', {"clientPartial": clientPartial})


def footerPartial(request):
    contact = Contact.objects.last()
    return render(request, 'tr/partials/_footer.html', {"contact": contact})
