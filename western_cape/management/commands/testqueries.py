from multiprocessing.resource_sharer import stop
import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand, CommandError
from western_cape.models import Stop, Line, Arrival, Direction, Train, TrainStop
from django.db.models import Count
from django.db.models import Q
import datetime

class Command(BaseCommand):
    help = 'Update Line'

    def add_arguments(self, parser):
        pass


    def minutesBetween(start_time, end_time):
        (s_hr, s_min) = start_time.split(':') #s_hr, s_min : start minute and start hour
        (e_hr, e_min) = end_time.split(':') #e_hr, e_min : end minute and start hour
        # start and end time objects
        s_dt = datetime.timedelta(hours=int(s_hr), minutes=int(s_min))
        e_dt = datetime.timedelta(hours=int(e_hr), minutes=int(e_min))
        difference = e_dt - s_dt
        result = str(difference).split(":")
        r_hr = int(result[0])
        if r_hr > 0:
            return r_hr*60 + int(result[1])
        else:
            return int(result[1])
    
    def handle(self, *args, **options):
        southWek = Line.objects.get(title="Southern", days="Wek")
        northWek = Line.objects.get(title="Northern", days="Wek")
        malmsWek = Line.objects.get(title="Malmesbury", days="Wek")
        centralWek = Line.objects.get(title="Central", days="Wek")
        worcesWek = Line.objects.get(title="Worcester", days="Wek")
        capefltsWek = Line.objects.get(title="Cape Flats", days="Wek")


        inboundNorth = Direction.objects.filter(title="In").get(line=northWek)
        outboundNorth = Direction.objects.filter(title="On").get(line=northWek)

        arriveNorth = Arrival.objects.filter(train__direction_id__line=northWek).order_by('train__train_number', 'arrival_time')
        
        trainTest = Train.objects.filter(
            Q(stops__title__contains="VASCO")
        ).values_list('train_number', flat=True)
        trainTest1 = Train.objects.filter(
            Q(stops__title__contains="SOMERSET WEST")
        ).values_list('train_number', flat=True)
        
        # print(trainTest)
        # print()
        # print(trainTest1)

        matches = set(list(trainTest)) & set(list(trainTest1))

        arrivals = Arrival.objects.filter(
            train__train_number__in=matches
        ).filter(
            arrival_time__startswith="17",
            # arrival_time__endswith=endtime
        ).order_by(
            'train__train_number'
        ).values(
            'train__train_number'
        ).annotate(
            count=Count('train__train_number')
        )
        
        routes = []
        for arrival in arrivals:
            values = list(arrival.values())
            route = dict()
            trainStops = arriveNorth.filter(train__train_number=values[0])
            for arrival in trainStops:
                route[arrival.stop.title] = str(arrival.arrival_time)
            print(route)    
            routes.append(route)
            print()
        print(len(routes))
