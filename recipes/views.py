from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Deyvison',
    })
