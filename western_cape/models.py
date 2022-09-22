from django.db import models
import uuid

# Create your models here.
class Line(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False, unique=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    OPERATION_DAYS = (
        ('Wek', "Weekdays"),
        ('Sun', "Sundays"),
        ('Sat', "Saturdays"),
        ('Hol', "Public Holidays"),
    )
    LINE_NUMBER = (
        (1, "ONE"),
        (2, "TWO"),
    )
    # direction = models.ForeignKey('Direction',default=uuid.uuid4, on_delete=models.CASCADE)
    days = models.CharField(max_length=3, choices=OPERATION_DAYS, blank=True, null=True)
    number = models.IntegerField(default=1, blank=False, null=False, choices=LINE_NUMBER)
    # train_stop_time = models.ForeignKey('Arrival', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self) :
        return self.title + ": " + self.get_days_display()

class Stop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    line = models.ManyToManyField(Line)
    interchange=models.BooleanField(default=False, blank=False, null=False)
    # switch=models.CharField(default=False)
    def __str__(self) :
        return self.title

class Direction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False, unique=True)
    DIRECTION_OPTIONS = (
        ('In', "Inbound"),
        ('On', "Outbound"),
    )
    title = models.CharField(max_length=2, blank=False, null=False, choices=DIRECTION_OPTIONS)
    stops = models.ManyToManyField(Stop)
    # trains = models.ManyToManyField('Train')
    line = models.ForeignKey(Line, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.line.title + ": " + self.get_title_display()

class TrainStop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False, unique=True)
    stops = models.ManyToManyField(Stop, blank=True)
    train_number = models.CharField(max_length=10, blank=True, null=True)
    only_stops_at =models.ManyToManyField('Arrival')
    def __str__(self):
        return self.train_number


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
        if self.arrival_time is None:
            return self.train.train_number + " starts at " + self.stop.title #+ self.arrival_time
        else:
            return self.train.train_number + " arriaves to " + self.stop.title +" at "+ self.arrival_time

class GraphEdge(models.Model):
    stop_from=models.CharField(max_length=200, blank=False, null=False)
    stop_to=models.CharField(max_length=200, blank=False, null=False)
    cost=models.IntegerField(default=0, blank=False, null=False)
    lines=models.ManyToManyField(Line)
    def __str__(self) :
        return self.stop_from + "   --->   " + self.stop_to + "   =   " + str(self.cost)