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
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker
    articleGathererFormExample=ArticleGathererForm(prefix='article___NUMBER__')
    articleGathererForms=[]
    if request.method == 'POST': # formularz został przesłany
        invoiceForm = InvoiceForm(request.POST, prefix='invoice') # powiązanie formularza z przesłanymi danymi
        if invoiceForm.is_valid():
            data = invoiceForm.cleaned_data
            invoice=invoiceForm.save()
            for i in range(data['NumberOfArticles']):
                articleGathererForm=ArticleGathererForm(request.POST, prefix='article_'+str(i+1))
                articleGathererForms.append(articleGathererForm)
                if articleGathererForm.is_valid():
                    articleGatherer=articleGathererForm.save(commit=False)
                    articleGatherer.Invoice=invoice
                    articleGatherer.save()
                else:
                    context={'InvoiceForm':invoiceForm, 'ArticleGathererForms' : articleGathererForms, 'ArticleGathererFormExample' : articleGathererFormExample, 'isWorker':isWorker}
                    return render(request, 'invoice_add.html', context) 
					
            return redirect('invoice.views.List')

        else:

            for i in range(int(invoiceForm.hidden_fields()[0].value())):
                    articleGathererForms.append(ArticleGathererForm(request.POST, prefix='article_'+str(i+1)))
    else:
        invoiceForm = InvoiceForm(prefix='invoice')
        articleGathererForms=[ArticleGathererForm(prefix='article_1')]
           
    context={'InvoiceForm':invoiceForm, 'ArticleGathererForms' : articleGathererForms, 'ArticleGathererFormExample' : articleGathererFormExample, 'isWorker':isWorker}
    return render(request, 'invoice_add.html', context)

def Delete(request):
    if request.GET.get('id'):
        invoice=Invoice.objects.filter(id=request.GET['id'])
        if invoice:
            invoice[0].delete()
    return redirect('invoice.views.List')
