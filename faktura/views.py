from django.shortcuts import render
from django.http import HttpResponse
from models import *

# Create your views here.

def index(request):
    Texts=Text.objects.all()
    context={'Texts': Texts}
    return render(request, 'index.html', context)
