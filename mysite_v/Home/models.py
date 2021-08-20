from django.db import models
from django.db import models
# Create your models here.
class Contacts(models.Model):
    
    Name = models.CharField(max_length=30)
    email= models.EmailField()
    phone= models.CharField(max_length=30)
    desc= models.TextField()
    
    def _str_(self):
        return self.name
