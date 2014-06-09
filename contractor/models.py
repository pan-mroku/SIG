from django.db import models
from django.forms import ModelForm

class Contractor(models.Model):
    Name=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Supplier=models.BooleanField(default=False)

    def __unicode__(self):
        if self.Supplier:
            return self.Name+' '+self.Address+' Supplier'
        return self.Name+' '+self.Address+' Buyer'
            
    

class ContractorForm(ModelForm):
    class Meta:
        model=Contractor
        fields='__all__'
