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
        invoiceForm = InvoiceForm(request.POST, prefix='invoice') # powiązanie formularza z przesłanymi danymi
        if invoiceForm.is_valid():
            invoice=invoiceForm.save()
            print str(invoiceForm)
            print str(invoiceForm.NumberOfArticles)
            for i in invoiceForm.NumberOfArticles:
                articleGathererForm=ArticleGathererForm(request.POST, prefix='article_'+str(i))
                if articleGathererForm.is_valid():
                    articleGatherer=articleGathererForm.save(commit=False)
                    articleGatherer.Invoice=invoice
                    articleGatherer.save()

            return redirect('invoice.views.List')

        else:
            articleGathererForms=[]
            for i in invoiceForm.NumberOfArticles:
                articleGathererForms.append(ArticleGathererForm(request.POST, prefix='article_'+str(i)))
    else:
        invoiceForm = InvoiceForm(prefix='invoice')
        articleGathererForms=[ArticleGathererForm(prefix='article_1')]
#        invoiceForm.NumberOfArticles=1
		
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker         
    context={'InvoiceForm':invoiceForm, 'ArticleGathererForms' : articleGathererForms, 'isWorker':isWorker}
    return render(request, 'invoice_add.html', context)

def Delete(request):
    if request.GET.get('id'):
        invoice=Invoice.objects.filter(id=request.GET['id'])
        if invoice:
            invoice[0].delete()
    return redirect('invoice.views.List')
