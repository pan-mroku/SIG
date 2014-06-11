from django.db import models

# Create your models here.

# 0 - client
# 1 - worker
class UserType(models.Model):
    name = models.CharField(max_length=120)
    isWorker = models.BooleanField(default=False)
    isWorker.editable=True
    
    def __unicode__(self):
        return self.name
