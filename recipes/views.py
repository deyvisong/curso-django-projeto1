from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Deyvison',
    })

def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return HttpResponse('SOBRE')
