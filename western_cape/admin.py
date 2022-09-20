from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Line)
admin.site.register(models.Direction)
admin.site.register(models.Arrival)
admin.site.register(models.Stop)
admin.site.register(models.Train)
admin.site.register(models.TrainStop)
admin.site.register(models.GraphEdge)