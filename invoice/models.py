from django.db import models
from django.forms import ModelForm, ValidationError, ModelMultipleChoiceField

class ArticleGatherer(models.Model):
    Article=models.ForeignKey('article.Article')
    Quantity=models.PositiveSmallIntegerField(default=1)

class Invoice(models.Model):
    Contractor=models.ForeignKey('contractor.Contractor')
    Articles=models.ManyToManyField('ArticleGatherer')
    DateOfSale=models.DateField(auto_now_add=True)
    PAYMENT_CHOICES=(
        ('CASH', 'Cash'),
        ('TRANSFER', 'Transfer'),
    )
    MethodOfPayment=models.CharField(max_length=8, choices=PAYMENT_CHOICES, default='CASH')
    DateOfPayment=models.DateField()

    def __unicode__(self):
        out=self.Contractor.Name+' '+str(self.DateOfSale)
        #for article in self.Articles:
        #    out=out+'\n'+article.Article.Code+' '+article.Article.Name+' '+article.Article.Price+' '+article.Quantity
        out=out+'\n'+self.MethodOfPayment+str(self.DateOfPayment)
        return out


from article.models import Article

class InvoiceForm(ModelForm):
    Articles=ModelMultipleChoiceField(queryset=Article.objects.all())
    class Meta:
        model=Invoice
        exclude=['Articles']

