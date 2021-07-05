from core.views import home,mb
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='index'),
    path('mb/', mb, name='mb')
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)