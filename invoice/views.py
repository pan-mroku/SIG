# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect

from models import *
from register.models import UserType

def List(request):
    invoices=Invoice.objects.all()
    context={'Invoices' : invoices}
    return render(request, 'invoice_list.html',context)

def Edit(request):
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

    context={'InvoiceForm':invoiceForm}
    return render(request, 'invoice_edit.html', context)

from article.models import Article

def Add(request):
    if request.method == 'POST': # formularz został przesłany
        invoiceForm = InvoiceForm(request.POST) # powiązanie formularza z przesłanymi danymi
        if invoiceForm.is_valid():
            gatherer=[]
            for articleid in request.POST['Articles']:
                article=Article.objects.get(pk=articleid)
                articleGatherer=ArticleGatherer(Article=article)
                articleGatherer.save()
                gatherer.append(articleGatherer)
            invoice=invoiceForm.save()
            for article in gatherer:
                invoice.Articles.append(article)
            invoice.save()
            
            return redirect('invoice.views.List')
        
    else:
        invoiceForm = InvoiceForm()
        
    context={'InvoiceForm':invoiceForm}
    return render(request, 'invoice_add.html', context)

def Delete(request):
    if request.GET.get('id'):
        invoice=Invoice.objects.filter(id=request.GET['id'])
        if invoice:
            invoice[0].delete()
    return redirect('invoice.views.List')
