from django.db import models
from django.forms import ModelForm, ValidationError

class Article(models.Model):
    Code=models.CharField(max_length=10)
    Name=models.CharField(max_length=200)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Availability=models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.Name+' '+str(self.Price)


class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields='__all__'

    def clean_Price(self):
        price = self.cleaned_data['Price']
        if price < 0.01:
            raise ValidationError(u"Wrong price!")
        return price

    def clean_Code(self):
        code=self.cleaned_data['Code']
        if code=='':
            code=self.pk
        return code
