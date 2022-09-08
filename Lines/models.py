from pickle import FALSE
from tkinter import CASCADE
from uuid import uuid4
from django.db import models
import uuid

# Create your models here.
class Line(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, null=False, blank=False)
    #startingStop =
    #destinationStop = 
    #stops
    #trains
    #schedule
    available = models.BooleanField(blank=False, null=False)

