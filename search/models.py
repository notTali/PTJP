from django.db import models
import uuid

from western_cape.models import Arrival

# Create your models here.
class Search(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    start_stop = models.CharField(max_length=200, null=False, blank=False)
    end_stop = models.CharField(max_length=200, null=False, blank=False)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

class Result(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False, unique=True)
    title = models.CharField(default="",max_length=200, null=False, blank=False)
    result = models.ManyToManyField(Arrival)