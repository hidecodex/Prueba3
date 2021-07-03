from django.shortcuts import render

# Create your views here.
def home (request):
    data = {}
    return render(request, 'home.html', data)


    """
    agregar

    def (nombre pagina) (request):
    data = {}
    return render(request, 'home.html', data)
    """