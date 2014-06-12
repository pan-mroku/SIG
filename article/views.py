# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import *
from register.models import UserType

def List(request):
#guest
    isWorker=False
    if not request.user.is_authenticated():
        articles=Article.objects.filter(Availability=True)		
    else:
		try:
			usertype = UserType.objects.get(name=request.user.username)
			isWorker = usertype.isWorker
			if usertype is not None and isWorker:
				articles=Article.objects.all()
			else:
				articles=Article.objects.filter(Availability=True)	
		except Exception as e:
				articles=Article.objects.filter(Availability=True)
		
    context={'Articles': articles, 'isWorker':isWorker}
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
            usertype = UserType.objects.get(name=request.user.username)
            article=Article.objects.get(id=request.GET['id'])
            if article and usertype.isWorker:
                articleForm=ArticleForm(instance=article)
            else:
                return redirect('article.views.List')
        else:
            return redirect('article.views.List')


    context={'ArticleForm':articleForm}
    return render(request, 'article_edit.html', context)
    
def Add(request):
    isWorker=False
    if request.method == 'POST': # formularz został przesłany
        articleForm = ArticleForm(request.POST) # powiązanie formularza z przesłanymi danymi
        if articleForm.is_valid():
            articleForm.save()
            
            return redirect('article.views.List')
        
    else:
        articleForm = ArticleForm()
        usertype = UserType.objects.get(name=request.user.username)
        isWorker = usertype.isWorker    
    context={'ArticleForm':articleForm, 'isWorker':isWorker}
    return render(request, 'article_add.html', context)

def Delete(request):
    if request.GET.get('id'):
        usertype = UserType.objects.get(name=request.user.username)
        article=Article.objects.get(id=request.GET['id'])
        if article and usertype.isWorker:
            article.delete()
    return redirect('article.views.List')
