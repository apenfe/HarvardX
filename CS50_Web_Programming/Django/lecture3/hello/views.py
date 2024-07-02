from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def adrian(request):
    return HttpResponse("Hola, Adrián")

def greet(request, name):
    return HttpResponse(f"Hello, {name.title()}")