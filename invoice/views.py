from django.shortcuts import render

from models import *

# Create your views here.

def List(request):
    Texts=Text.objects.all()
    context={'Texts': Texts}
    return render(request, 'invoice_list.html', context)
