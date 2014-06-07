from django.db import models
from django.forms import ModelForm, ValidationError

class Article(models.Model):
    Name=models.CharField(max_length=200)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Availability=models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.Name+' '+str(self.Price)


class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields='__all__'
        hidden='id'

    def clean_Price(self):
        price = self.cleaned_data['Price']
        if price < 0.01:
            raise ValidationError(u"Wrong price!")
        return price
