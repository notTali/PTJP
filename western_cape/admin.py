from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Line)
admin.site.register(models.Direction)
admin.site.register(models.Route)
admin.site.register(models.Stop)
# admin.site.register(models.Line)