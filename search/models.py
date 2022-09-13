from django.db import models
import uuid

# Create your models here.
class Search(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    start_stop = models.CharField(max_length=200, null=False, blank=False)
    end_stop = models.CharField(max_length=200, null=False, blank=False)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)