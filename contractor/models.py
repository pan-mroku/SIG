from django.db import models
from django.forms import ModelForm

class Contractor(models.Model):
    Name=models.CharField(max_length=200)
    Login=models.ForeignKey('register.UserType', null=True)
    Address=models.CharField(max_length=200)
    Supplier=models.BooleanField(default=False)

    def __unicode__(self):
        return self.Name+' '+self.Address
            
    

class ContractorFormWorker(ModelForm):
    class Meta:
        model=Contractor

class ContractorFormClient(ModelForm):
    class Meta:
        model=Contractor
        exclude=['Supplier', 'Login']
