from django.db import models

# Create your models here.

class Text(models.Model):
    Content=models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.Content
