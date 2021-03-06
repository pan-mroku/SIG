# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.utils import timezone

from models import *
from register.models import UserType

def List(request):        
    usertype = UserType.objects.get(name=request.user.username)
    
    if usertype.isWorker:
        invoices=Invoice.objects.all()
    else:
        contractors=Contractor.objects.filter(Login=usertype)
        invoices=[]
        for contractor in contractors:
            invoices.extend(Invoice.objects.filter(Contractor=contractor))
    
    context={'Invoices' : invoices, 'isWorker':usertype.isWorker}
    return render(request, 'invoice_list.html',context)

def View(request):
    if request.method == 'POST':
        invoice=Invoice.objects.get(id=request.POST['id'])
        articles=ArticleGatherer.objects.filter(Invoice=invoice)
        context={'Invoice' : invoice, 'ArticleGatherers' : articles}
        return render(request, 'invoice_view.html', context)
        
    return redirect('invoice.views.List')

def SetDateOfPayment(request):
    if request.method == 'POST':
        invoice=Invoice.objects.get(pk=request.POST['id'])
        invoice.DateOfPayment=timezone.localtime(timezone.now()).date()
        invoice.save()
    return redirect('invoice.views.List')

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
                
           
                               
            #skoro przeszło wszystkie artykuły i jest ok, to można zapisać, ale tylko jeśli są jakieś artykuły!
            if articleGathererForms:
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
                i=1
                for article in ArticleGatherer.objects.filter(Invoice=invoice):
                    articleGathererForms.append(ArticleGathererForm(instance=article, prefix='article_'+str(i)))
                    i=i+1
                if isWorker and invoice.DateOfPayment == None:
                    invoiceForm=InvoiceForm(instance=invoice, prefix='invoice', initial={'NumberOfArticles':len(articleGathererForms)})
                elif invoice.Contractor.Login==usertype and invoice.Contractor.Supplier==False and invoice.DateOfPayment == None:
                    invoiceForm=InvoiceForm(instance=invoice, prefix='invoice', initial={'NumberOfArticles':len(articleGathererForms)})
                else:
                    return redirect('invoice.views.List')
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
    articleGathererFormExample.fields['Article'].queryset = Article.objects.filter(Availability=True)
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
                
            if articleGathererForms:
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
            invoiceForm.fields['Contractor'].queryset = Contractor.objects.filter()
        else:
            invoiceForm.fields['Contractor'].queryset = Contractor.objects.filter(Login=usertype, Supplier=False)

        articleGathererForm=ArticleGathererForm(prefix='article_1')
        if not isWorker:
          articleGathererForm.fields['Article'].queryset = Article.objects.filter(Availability=True)

        articleGathererForms=[articleGathererForm] 
           
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
