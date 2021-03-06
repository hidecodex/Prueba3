from core.views import Deslogeo, Logeando, SignIn, home,mb,cpu,gpu,psu,ram,hdd,ssd,m2,Registros,admin,SignUp
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='index'),
    path('mb/', mb, name='mb'),
    path('cpu/', cpu, name='cpu'),
    path('gpu/', gpu, name='gpu'),
    path('psu/', psu, name='psu'),
    path('ram/', ram, name='ram'),
    path('hdd/', hdd, name='hdd'),
    path('ssd/', ssd, name='ssd'),
    path('m2/', m2, name='m2'),
    path('admin2/', admin, name='admin'),
    # Sign In
    path('signin/', SignIn, name='SignIn'),
    path('signup/', SignUp, name='SignUp'),
    path('registro/', Registros, name='Registros'),
    path('signin/logeando/', Logeando, name='Logeando'),
    path('signin/deslogeando/', Deslogeo, name='Deslogeo'),

]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)