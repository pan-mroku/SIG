from django.shortcuts import render
from models import *

# Create your views here.

def List(request):
    articles=Article.objects.all()
    context={'Articles': articles}
    return render(request, 'article_list.html', context)
