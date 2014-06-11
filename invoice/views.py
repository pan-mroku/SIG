# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect

from models import *
from register.models import UserType

def List(request):
    isWorker=False
    invoices=Invoice.objects.all()
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker 
    context={'Invoices' : invoices, 'isWorker':isWorker}
    return render(request, 'invoice_list.html',context)

# def View(request):
#     if request.method == 'POST':
#         invoice=Invoice.objects.get(id=request.POST['invoiceId'])
#         invoiceForm=InvoiceForm(request.POST, instance=invoice)
#         articles=ArticleGatherer.objects.get(id=request.POST['articlesId'])
        

def Edit(request):
    isWorker=False
    if request.method == 'POST':
        invoice=Invoice.objects.get(id=request.POST['id'])
        invoiceForm=InvoiceForm(request.POST, instance=invoice)

        if invoiceForm.is_valid():
            invoiceForm.save()

            return redirect('invoice.views.List')

    else:
        if request.GET.get('id'):
            invoice=Invoice.objects.filter(id=request.GET['id'])
            if invoice:
                invoiceForm=InvoiceForm(instance=invoice[0])
            else:
                return redirect('invoice.views.List')
        else:
            return redirect('invoice.views.List')
			
	usertype = UserType.objects.get(name=request.user.username)
	isWorker = usertype.isWorker 
    context={'InvoiceForm':invoiceForm, 'isWorker':isWorker}
    return render(request, 'invoice_edit.html', context)

from article.models import Article

def Add(request):
    isWorker=False
    if request.method == 'POST': # formularz został przesłany
        invoiceForm = InvoiceForm(request.POST) # powiązanie formularza z przesłanymi danymi
        if invoiceForm.is_valid():
            invoice=invoiceForm.save()
            gatherer=[]
            for articleid in request.POST['Articles']:
                article=Article.objects.get(pk=articleid)
                articleGatherer=ArticleGatherer(Article=article, Invoice=invoice)
                articleGatherer.save()
            # for article in gatherer:
            #     invoice.Articles.append(article)
            # invoice.save()
            
            return redirect('invoice.views.List')
        
    else:
        invoiceForm = InvoiceForm()
		
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker         
    context={'InvoiceForm':invoiceForm, 'isWorker':isWorker}
    return render(request, 'invoice_add.html', context)

def Delete(request):
    if request.GET.get('id'):
        invoice=Invoice.objects.filter(id=request.GET['id'])
        if invoice:
            invoice[0].delete()
    return redirect('invoice.views.List')
