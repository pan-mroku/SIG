# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect

from models import *
from register.models import UserType

def List(request):
    usertype = UserType.objects.get(name=request.user.username)
    
    if usertype.isWorker:
        invoices=Invoice.objects.all()
    else:
#        contractor=Contractor.objects.filter(Login=usertype.pk)
#        for 
        invoices=Invoice.objects.all()
    
    context={'Invoices' : invoices, 'isWorker':usertype.isWorker}
    return render(request, 'invoice_list.html',context)

# def View(request):
#     if request.method == 'POST':
#         invoice=Invoice.objects.get(id=request.POST['invoiceId'])
#         invoiceForm=InvoiceForm(request.POST, instance=invoice)
#         articles=ArticleGatherer.objects.get(id=request.POST['articlesId'])
        
def Edit(request):
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker 
    
    articleGathererFormExample=ArticleGathererForm(prefix='article___NUMBER__')
    articleGathererForms=[]
        
    if request.method == 'POST':
        invoice=Invoice.objects.get(id=request.POST['id'])
        invoiceForm = InvoiceForm(request.POST, prefix='invoice', instance=invoice) # powiązanie formularza z przesłanymi danymi
        if invoiceForm.is_valid():
            data = invoiceForm.cleaned_data
            invoice=invoiceForm.save(commit=False)
            for i in range(data['NumberOfArticles']):
                articleGathererForm=ArticleGathererForm(request.POST, prefix='article_'+str(i+1))
                articleGathererForms.append(articleGathererForm)

            for articleGathererForm in articleGathererForms:
                if not articleGathererForm.is_valid():
                    context={'InvoiceForm':invoiceForm, 'ArticleGathererForms' : articleGathererForms, 'ArticleGathererFormExample' : articleGathererFormExample, 'isWorker':isWorker}
                    return render(request, 'invoice_add.html', context)
                
           
                               
            #skoro przeszło wszystkie artykuły i jest ok, to można zapisać
            invoice.save()
            for articleGathererForm in articleGathererForms:
                articleGatherer=articleGathererForm.save(commit=False)
                articleGatherer.Invoice=invoice
                articleGathererForm.save()
					
            return redirect('invoice.views.List')

    else:
        if request.GET.get('id'):
            invoice=Invoice.objects.filter(pk=request.GET['id'])
            if invoice:
                invoice=invoice[0]
                if isWorker:
                    invoiceForm=InvoiceForm(instance=invoice, prefix='invoice')
                elif invoice.Contractor.Login==usertype and invoice.Contractor.Supplier==False and (invoice.DateOfPayment == None):
                    invoiceForm=InvoiceForm(instance=invoice, prefix='invoice')
                else:
                    return redirect('invoice.views.List')
                i=1
                for article in ArticleGatherer.objects.filter(Invoice=invoice):
                    articleGathererForms.append(ArticleGathererForm(instance=article, prefix='article_'+str(i)))
                    i=i+1
            else:
                return redirect('invoice.views.List')
        else:
            return redirect('invoice.views.List')
    
    context={'InvoiceForm':invoiceForm, 'ArticleGathererForms': articleGathererForms, 'ArticleGathererFormExample' : articleGathererFormExample}
    return render(request, 'invoice_edit.html', context)

from article.models import Article
from contractor.models import Contractor

def Add(request):
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker

    articleGathererFormExample=ArticleGathererForm(prefix='article___NUMBER__')
    articleGathererForms=[]
    
    if request.method == 'POST': # formularz został przesłany
        invoiceForm = InvoiceForm(request.POST, prefix='invoice') # powiązanie formularza z przesłanymi danymi
        if invoiceForm.is_valid():
            data = invoiceForm.cleaned_data
            invoice=invoiceForm.save(commit=False)
            for i in range(data['NumberOfArticles']):
                articleGathererForm=ArticleGathererForm(request.POST, prefix='article_'+str(i+1))
                articleGathererForms.append(articleGathererForm)
                
            for articleGathererForm in articleGathererForms:
                if  not articleGathererForm.is_valid():
                    context={'InvoiceForm':invoiceForm, 'ArticleGathererForms' : articleGathererForms, 'ArticleGathererFormExample' : articleGathererFormExample, 'isWorker':isWorker}
                    return render(request, 'invoice_add.html', context)
                
                                    
            #skoro przeszło wszystkie artykuły i jest ok, to można zapisać
            invoice.save()
            for articleGathererForm in articleGathererForms:
                articleGatherer=articleGathererForm.save(commit=False)
                articleGatherer.Invoice=invoice
                articleGathererForm.save()
					
            return redirect('invoice.views.List')

        else:

            for i in range(int(invoiceForm.hidden_fields()[0].value())):
                    articleGathererForms.append(ArticleGathererForm(request.POST, prefix='article_'+str(i+1)))
    else:
        invoiceForm = InvoiceForm(prefix='invoice')
        if isWorker:
            invoiceForm.fields['Contractor'].queryset = Contractor.objects.filter(Supplier=True)
        else:
            invoiceForm.fields['Contractor'].queryset = Contractor.objects.filter(Login=usertype, Supplier=False)

        articleGathererForms=[ArticleGathererForm(prefix='article_1')]
           
    context={'InvoiceForm':invoiceForm, 'ArticleGathererForms' : articleGathererForms, 'ArticleGathererFormExample' : articleGathererFormExample, 'isWorker':isWorker}
    return render(request, 'invoice_add.html', context)

def Delete(request):
    if request.GET.get('id'):
        usertype = UserType.objects.get(name=request.user.username)
        invoice=Invoice.objects.filter(id=request.GET['id'])
        if invoice:
            invoice=invoice[0]
            if usertype.isWorker:
                invoice.delete()
            elif invoice.Contractor.Login==usertype and invoice.Contractor.Supplier==False and (invoice.DateOfPayment == None):
                invoice.delete()
    return redirect('invoice.views.List')
