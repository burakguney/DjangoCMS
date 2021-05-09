from django.shortcuts import render
from django.http import HttpRequest
from .models import About, Faq, PrivacyPolicy, Contact

# Create your views here.


def home_en(request):
    return render(request, 'en/home.html')


def about_en(request):
    about = About.objects.last()
    return render(request, 'en/about.html', {'about': about})


def contact_en(request):
    contact = Contact.objects.last()
    return render(request, 'en/contact.html', {'contact': contact})


def faq_en(request):
    faqFirst = Faq.objects.first()
    faq = Faq.objects.all()[1:]
    return render(request, 'en/faq.html', {'faqFirst': faqFirst, 'faq': faq})


def privacyPolicy_en(request):
    privacyPolicy = PrivacyPolicy.objects.last()
    return render(request, 'en/privacyPolicy.html', {'privacyPolicy': privacyPolicy})


def getOffer_en(request):
    return render(request, 'en/getOffer.html')
