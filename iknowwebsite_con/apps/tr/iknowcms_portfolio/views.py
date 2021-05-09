from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator
from .models import Portfolio
# Create your views here.


def portfolioList(request):
    portfolioList = Portfolio.objects.all().order_by("-pk")
    paginator = Paginator(portfolioList, 6)
    page_number = request.GET.get("page")
    page_portfolioList = paginator.get_page(page_number)
    return render(request, 'tr/portfolio/portfolioList.html', {"page_portfolioList": page_portfolioList})


def portfolioSingle(request, portfolioSlug):
    portfolioSingle = Portfolio.objects.get(portfolioSlug=portfolioSlug)
    return render(request, 'tr/portfolio/portfolioSingle.html', {"portfolioSingle": portfolioSingle})


def portfolioPartial(request):
    portfolioPartial = Portfolio.objects.all().order_by("-pk")[:4]
    return render(request, 'tr/portfolio/portfolioPartial.html', {"portfolioPartial": portfolioPartial})
