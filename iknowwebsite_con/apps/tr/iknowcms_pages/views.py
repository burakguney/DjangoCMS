from django.shortcuts import render
from django.http import HttpRequest
from .models import About, Faq, PrivacyPolicy, Contact

# Create your views here.


def home(request):
    return render(request, 'tr/home.html')


def about(request):
    about = About.objects.last()
    return render(request, 'tr/about.html', {'about': about})


def contact(request):
    contact = Contact.objects.last()
    return render(request, 'tr/contact.html', {'contact': contact})


def faq(request):
    faqFirst = Faq.objects.first()
    faq = Faq.objects.all()[1:]
    return render(request, 'tr/faq.html', {'faqFirst': faqFirst, 'faq': faq})


def privacyPolicy(request):
    privacyPolicy = PrivacyPolicy.objects.last()
    return render(request, 'tr/privacyPolicy.html', {'privacyPolicy': privacyPolicy})


def getOffer(request):
    return render(request, 'tr/getOffer.html')
