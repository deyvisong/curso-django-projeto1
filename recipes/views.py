from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def home(request):
    ...
    return HttpResponse('HOME 2')

def contato(request):
    ...
    return HttpResponse('CONTATO')

def sobre(request):
    ...
    return HttpResponse('SOBRE')
