from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator
from .models import Portfolio
# Create your views here.


def portfolioList_en(request):
    portfolioList = Portfolio.objects.all().order_by("-pk")
    paginator = Paginator(portfolioList, 6)
    page_number = request.GET.get("page")
    page_portfolioList = paginator.get_page(page_number)
    return render(request, 'en/portfolio/portfolioList.html', {"page_portfolioList": page_portfolioList})


def portfolioSingle_en(request, portfolioSlug):
    portfolioSingle = Portfolio.objects.get(portfolioSlug=portfolioSlug)
    return render(request, 'en/portfolio/portfolioSingle.html', {"portfolioSingle": portfolioSingle})


def portfolioPartial_en(request):
    portfolioPartial = Portfolio.objects.all().order_by("-pk")[:11]
    return render(request, 'en/portfolio/portfolioPartial.html', {"portfolioPartial": portfolioPartial})
