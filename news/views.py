from django.shortcuts import render, get_object_or_404
from .models import News


def news_list(request):
    news = News.objects.all()

    return render(request, 'main/news/list.html', {
        'news': news,
    })


def news_detail(request, id, slug):
    article = get_object_or_404(
        News,
        id=id,
        slug=slug
    )

    related_news = News.objects.exclude(id=article.id)[:3]

    return render(request, 'main/news/detail.html', {
        'article': article,
        'related_news': related_news,
    })