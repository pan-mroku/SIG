# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import *
from register.models import UserType

def List(request):
    isWorker=False
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker
    if isWorker:
        contractors=Contractor.objects.all()
    else:
        contractors=Contractor.objects.filter(Login=usertype.pk, Supplier=False)
    context={'Contractors': contractors, 'isWorker':isWorker}
    return render(request, 'contractor_list.html', context)

def Edit(request):
    isWorker=False
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker
    if request.method == 'POST':
        contractor=Contractor.objects.get(id=request.POST['id'])
        if isWorker:
          contractorForm=ContractorFormWorker(request.POST, instance=contractor)
        else:
          contractorForm=ContractorFormClient(request.POST, instance=contractor)

        if contractorForm.is_valid():
            contractorForm.save()

            return redirect('contractor.views.List')

    else:
        if request.GET.get('id'):
            contractor=Contractor.objects.get(id=request.GET['id'])
            if contractor:
              if isWorker:
                contractorForm=ContractorFormWorker(instance=contractor)
              elif contractor.Login==usertype and contractor.Supplier==False:
                contractorForm=ContractorFormClient(instance=contractor)
              else:
                return redirect('contractor.views.List')
            else:
                return redirect('contractor.views.List')
        else:
            return redirect('contractor.views.List')

    context={'ContractorForm':contractorForm, 'isWorker':isWorker}
    return render(request, 'contractor_edit.html', context)
    
def Add(request):
    usertype = UserType.objects.get(name=request.user.username)
    isWorker = usertype.isWorker
    if request.method == 'POST': # formularz został przesłany
      supplier = request.POST.get('Supplier', False)      
      if isWorker:
        if request.POST['Login']=='':
          contractor = Contractor(Name=request.POST['Name'],Address=request.POST['Address'],Supplier=supplier)
        else:
          contractor = Contractor(Name=request.POST['Name'],Address=request.POST['Address'],Supplier=supplier,Login=UserType.objects.get(pk=request.POST['Login']))
        contractor.save()
      else:
        contractor = Contractor(Name=request.POST['Name'],Address=request.POST['Address'],Supplier=False,Login=UserType.objects.get(name=request.user.username))
        contractor.save()
      return redirect('contractor.views.List')	

    if isWorker:	
      context={'ContractorFormWorker':ContractorFormWorker(), 'isWorker':isWorker}
    else:
      context={'ContractorFormClient':ContractorFormClient(), 'isWorker':isWorker}
    
    return render(request, 'contractor_add.html', context)

def Delete(request):
    if request.GET.get('id'):
        usertype = UserType.objects.get(name=request.user.username)
        contractor=Contractor.objects.get(id=request.GET['id'])
        if contractor:
            if usertype.isWorker:
                contractor.delete()
            elif contractor.Login==usertype and contractor.Supplier==False:
                contractor.delete()
    return redirect('contractor.views.List')
