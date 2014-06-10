# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import *
from register.models import UserType

def List(request):
#guest
    e='Done!'
    if not request.user.is_authenticated():
        articles=Article.objects.filter(Availability=True)		
    else:
		try:
			usertype = UserType.objects.get(name=request.user.username)
			if usertype is not None and usertype.isWorker:
				articles=Article.objects.all()
			else:
				articles=Article.objects.filter(Availability=True)	
		except Exception as e:
				articles=Article.objects.filter(Availability=True)
		
    context={'Articles': articles, 'info':e}
    return render(request, 'article_list.html', context)

def Edit(request):
    if request.method == 'POST':
        article=Article.objects.get(id=request.POST['id'])
        articleForm=ArticleForm(request.POST, instance=article)

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

def Delete(request):
    if request.GET.get('id'):
        article=Article.objects.filter(id=request.GET['id'])
        if article:
            article[0].delete()
    return redirect('article.views.List')
