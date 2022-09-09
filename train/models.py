from email.policy import default
from django.db import models
import json

# Create your models here.
class Train(models.Model):
    number = models.CharField(null=True, blank=True, max_length=8)
    data = models.JSONField()
    
    def __str__(self):
        return "Train number "+self.number