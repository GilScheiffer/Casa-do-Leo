from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'galeria/index.html')
 
def imagem(request):
    return render(request, 'galeria/imagem.html')

def form(request):
    return render(request, 'galeria/form.html')

def casa_do_leo(request):
    return render(request, 'galeria/casa_do_leo.html')