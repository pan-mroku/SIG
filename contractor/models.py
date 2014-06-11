from django.db import models
from django.forms import ModelForm

class Contractor(models.Model):
    Name=models.CharField(max_length=200)
    Login=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Supplier=models.BooleanField(default=False)

    def __unicode__(self):
        if self.Supplier:
            return self.Name+' ('+self.Login+') '+self.Address+' Supplier'
        return self.Name+' '+self.Address+' Buyer'
            
    

class ContractorFormWorker(ModelForm):
    class Meta:
        model=Contractor

class ContractorFormClient(ModelForm):
    class Meta:
        model=Contractor
        exclude=['Supplier', 'Login']