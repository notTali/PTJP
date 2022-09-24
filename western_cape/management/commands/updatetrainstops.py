# updatetrainstops


import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand, CommandError
from western_cape.models import Stop, Line, Arrival, Direction, Train, TrainStop

class Command(BaseCommand):
    help = 'Update TrainStop model'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        centralWek = Line.objects.get(title="Central", days="Wek")
        outboundCentral = Direction.objects.filter(title="On").get(line=centralWek)


        # trainstops = TrainStop.objects.all()
        trains = Train.objects.filter(
            direction_id=outboundCentral,
        )
        
        for train in trains:
            tstop = []
            # get a list of arrivals + stops it goes to
            # print(train.train_number)
            
            # List of arrivals:
            arrivals = Arrival.objects.filter(
                train__train_number=train.train_number,
            ) 

            # form each arrival, get a list of stops:
            stops = []
            for arrival in arrivals:
                stops.append(arrival.stop)
                # print(arrival.stop)
            # print(stops)
            
            print(train.train_number, "Added...........................")

        #     for stp in arrival.only_stops_at.all():
        #         tstop.append(stp.stop)
        #     TrainStop.objects.get(
        #         train_number=arrival.train_number
        #     ).stops.set(tstop)
        #     print(arrival.train_number, "Added ....................") 


        # for arrival in trainstops:
        #     print(arrival)
        #     tstop = []
        #     for stp in arrival.only_stops_at.all():
        #         tstop.append(stp.stop)
        #     TrainStop.objects.get(
        #         train_number=arrival.train_number
        #     ).stops.set(tstop)
        #     print(arrival.train_number, "Added ....................")    
        