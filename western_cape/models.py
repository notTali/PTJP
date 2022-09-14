from django.db import models
import uuid

# Create your models here.
class Line(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    OPERATION_DAYS = (
        ('Wek', "Weekdays"),
        ('Sun', "Sundays"),
        ('Sat', "Saturdays"),
        ('Hol', "Public Holidays"),
    )
    # direction = models.ForeignKey('Direction',default=uuid.uuid4, on_delete=models.CASCADE)
    days = models.CharField(max_length=3, choices=OPERATION_DAYS, blank=True, null=True)
    # train_stop_time = models.ForeignKey('Arrival', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self) :
        return self.title + ": " + self.get_days_display()

class Stop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    line = models.ManyToManyField(Line)
    def __str__(self) :
        return self.title

class Direction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    DIRECTION_OPTIONS = (
        ('In', "Inbound"),
        ('On', "Outbound"),
    )
    title = models.CharField(max_length=2, blank=False, null=False, choices=DIRECTION_OPTIONS)
    stops = models.ManyToManyField(Stop)
    # trains = models.ManyToManyField('Train')
    line = models.ForeignKey(Line, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.title

class Train(models.Model): #can also be called a Route
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    train_number = models.CharField(max_length=10, blank=False, null=False)
    direction_id = models.ForeignKey(Direction, on_delete=models.CASCADE)
    stops = models.ManyToManyField(Stop, through='Arrival')
    
    def __str__(self) :
        return "Train " + self.train_number

class Arrival(models.Model): 
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    arrival_time = models.CharField(max_length=6, blank=True, null=True)
    platform_number = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.arrival_time