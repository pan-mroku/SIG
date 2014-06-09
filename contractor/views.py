# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import *

def List(request):
    contractors=Contractor.objects.all()
    context={'Contractors': contractors}
    return render(request, 'contractor_list.html', context)

def Edit(request):
    if request.method == 'POST':
        contractor=Contractor.objects.get(id=request.POST['id'])
        contractorForm=ContractorForm(request.POST, instance=contractor)

        if contractorForm.is_valid():
            contractorForm.save()

            return redirect('contractor.views.List')

    else:
        if request.GET.get('id'):
            contractor=Contractor.objects.filter(id=request.GET['id'])
            if contractor:
                contractorForm=ContractorForm(instance=contractor[0])
            else:
                return redirect('contractor.views.List')
        else:
            return redirect('contractor.views.List')

    context={'ContractorForm':contractorForm}
    return render(request, 'contractor_edit.html', context)
    
def Add(request):
    if request.method == 'POST': # formularz został przesłany
        contractorForm = ContractorForm(request.POST) # powiązanie formularza z przesłanymi danymi
        if contractorForm.is_valid():
            contractorForm.save()
            
            return redirect('contractor.views.List')
        
    else:
        contractorForm = ContractorForm()
        
    context={'ContractorForm':contractorForm}
    return render(request, 'contractor_add.html', context)

def Delete(request):
    if request.GET.get('id'):
        contractor=Contractor.objects.filter(id=request.GET['id'])
        if contractor:
            contractor[0].delete()
    return redirect('contractor.views.List')
