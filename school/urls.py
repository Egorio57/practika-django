from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from school.views import custom_404, custom_500

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls', namespace='news')),
    path('', include('services.urls', namespace='services')),
    path('', include('home.urls', namespace='home')),
    path(
    'contacts/',
    include('contacts.urls')
),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)

handler404 = custom_404
handler500 = custom_500



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
