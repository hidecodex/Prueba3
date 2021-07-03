from core.views import home
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='index')
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)