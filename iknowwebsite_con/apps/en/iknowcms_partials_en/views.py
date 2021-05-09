from django.shortcuts import render
from django.http import HttpRequest
from .models import Testimonial, Client, Carousel
from apps.en.iknowcms_pages_en.models import Contact

# Create your views here.


def carouselPartial_en(request):
    carouselPartial = Carousel.objects.all()
    return render(request, 'en/partials/home/carouselPartial.html', {"carouselPartial": carouselPartial})


def carouselSingle_en(request, carouselSlug):
    carouselSingle = Carousel.objects.get(carouselSlug=carouselSlug)
    return render(request, 'en/partials/home/carouselSingle.html', {"carouselSingle": carouselSingle})


def testimonialPartial_en(request):
    testimonialPartial = Testimonial.objects.all()
    return render(request, 'en/partials/home/testimonialPartial.html', {"testimonialPartial": testimonialPartial})


def clientPartial_en(request):
    clientPartial = Client.objects.all()
    return render(request, 'en/partials/home/clientPartial.html', {"clientPartial": clientPartial})


def footerPartial_en(request):
    contact = Contact.objects.last()
    return render(request, 'en/partials/_footer.html', {"contact": contact})
