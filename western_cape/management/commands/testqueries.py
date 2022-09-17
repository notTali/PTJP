from multiprocessing.resource_sharer import stop
import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand, CommandError
from western_cape.models import Stop, Line, Arrival, Direction, Train
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

        # print(arriveNorth)
        temp = Arrival.objects.filter(
            train__direction_id__line=northWek
        ).filter(
            # train__direction_id__stops__title__startswith="WOODSTOCK"
            Q(stop__title="WOODSTOCK") & Q(train__direction_id__stops__title__startswith="MAITLAND")
            
        ).filter(
            # train__direction_id__stops__title__startswith="KRAAIFONTEIN"
        ).filter(
            arrival_time__startswith="16",
            # arrival_time__endswith="3"
        ).order_by('train__train_number'
        ).values('train__train_number'
        ).annotate(count=Count('train__train_number'))
        
        routes = []
        for t in temp:
            vls = list(t.values())
            # print(list(t.values()))
            route = dict()
            trainStops = arriveNorth.filter(train__train_number=vls[0])
            for arrival in trainStops:
                print(arrival.stop.title, arrival.arrival_time)
                route[arrival.stop.title] = arrival.arrival_time
            routes.append(route)
            print(route)
            print()
        # print(routes, len(temp))
        
# Code to get stops in any line
        # df = pd.read_excel("static/sheets/Stops_per_Line.xlsx", engine='openpyxl')
        # for column in df.columns:
        #     col_data = df[column]
        #     aLine=None
        #     if column == "Southern":
        #         aLine = southWek
        #     elif column == "Northern":
        #         aLine = northWek
        #     elif column == "Malmesbury":
        #         aLine = malmsWek
        #     elif column == "Central":
        #         aLine = centralWek
        #     elif column == "Worcester":
        #         aLine = worcesWek
        #     elif column == "Cape Flats":
        #         aLine = capefltsWek
            
        #     print(aLine.title)
        #     for row in range(len(col_data)):
        #         row_data = col_data[row]
        #         if type(row_data) != float:
        #             print(row_data)
        #     print()