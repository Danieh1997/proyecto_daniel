from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola, soy Daniel</h1><p>Y este es mi primer proyecto en Django</p>")