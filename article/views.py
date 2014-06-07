# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import *

def List(request):
    articles=Article.objects.all()
    context={'Articles': articles}
    return render(request, 'article_list.html', context)

def Edit(request):
    if request.method == 'POST':
        articleForm=ArticleForm(request.POST)

        if articleForm.is_valid():
            articleForm.save()

            return redirect('article.views.List')

    else:
        if request.GET.get('id'):
            article=Article.objects.filter(id=request.GET['id'])
            if article:
                articleForm=ArticleForm(instance=article[0])
            else:
                return redirect('article.views.List')
        else:
            return redirect('article.views.List')

    context={'ArticleForm':articleForm}
    return render(request, 'article_edit.html', context)
    
def Add(request):
    if request.method == 'POST': # formularz został przesłany
        articleForm = ArticleForm(request.POST) # powiązanie formularza z przesłanymi danymi
        if articleForm.is_valid():
            articleForm.save()
            
            return redirect('article.views.List')
        
    else:
        articleForm = ArticleForm()
        
    context={'ArticleForm':articleForm}
    return render(request, 'article_add.html', context)
