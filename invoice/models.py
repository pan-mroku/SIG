from django.db import models
from django import forms

class ArticleGatherer(models.Model):
    Invoice=models.ForeignKey('Invoice')
    Article=models.ForeignKey('article.Article')
    Quantity=models.PositiveSmallIntegerField(default=1)

class Invoice(models.Model):
    Contractor=models.ForeignKey('contractor.Contractor')
    Articles=models.ManyToManyField('article.Article', through='ArticleGatherer')
    DateOfSale=models.DateField(auto_now_add=True)
    PAYMENT_CHOICES=(
        ('CASH', 'Cash'),
        ('TRANSFER', 'Transfer'),
    )
    MethodOfPayment=models.CharField(max_length=8, choices=PAYMENT_CHOICES, default='CASH')
    DateOfPayment=models.DateField(null=True)

    def __unicode__(self):
        out=self.Contractor.Name+' '+str(self.DateOfSale)
        out=out+'\n'+self.MethodOfPayment+str(self.DateOfPayment)
        return out
from article.models import Article

class ArticleGathererForm(forms.ModelForm):
    Quantity=forms.IntegerField(widget=forms.NumberInput(attrs={'min':'1'}), initial=1)
    class Meta:
        model=ArticleGatherer
        exclude=['Invoice']

class InvoiceForm(forms.ModelForm):
    NumberOfArticles=forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    class Meta:
        model=Invoice
        exclude=['Articles', 'DateOfPayment']

