from django.shortcuts import render
from news.models import News
from services.models import Service
from .models import CompanyInfo


def home(request):

    latest_news = News.objects.order_by('-created_at')[:3]

    main_services = Service.objects.all()[:3]

    company = CompanyInfo.objects.first()

    context = {
        'latest_news': latest_news,
        'main_services': main_services,
        'company': company,
    }

    return render(request, 'main/home/home.html', context)