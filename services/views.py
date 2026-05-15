from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCategory


def services_list(request):
    category_slug = request.GET.get('category')

    categories = ServiceCategory.objects.all()

    services = Service.objects.select_related('category')

    selected_category = None

    if category_slug:
        selected_category = get_object_or_404(ServiceCategory, slug=category_slug)
        services = services.filter(category=selected_category)

    return render(request, 'main/services/list.html', {
        'categories': categories,
        'services': services,
        'selected_category': selected_category,
    })


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)

    related_services = Service.objects.exclude(id=service.id)[:3]


    return render(request, 'main/services/detail.html', {
        'service': service,
        'related_services': related_services,
    })