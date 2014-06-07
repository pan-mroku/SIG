from django.db import models

# Create your models here.

class Article(models.Model):
    Name=models.CharField(max_length=200)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __unicode__(self):
        return self.Name+' '+str(self.Price)
