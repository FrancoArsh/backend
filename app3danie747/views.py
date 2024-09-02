from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de app3danie747</h1>")

def texto(requesto):
    html="<h1>Soy un texto de la app3danie747</h1>"
    return HttpResponse(html)
