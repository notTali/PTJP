from turtle import title
import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand, CommandError
from western_cape.models import Stop, Line, Arrival, Direction, Train
from django.db.models import Q

class Command(BaseCommand):
    help = 'Update Line'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        southWek = Line.objects.get(title="Southern", days="Wek")
        northWek = Line.objects.get(title="Northern", days="Wek")
        malmsWek = Line.objects.get(title="Malmesbury", days="Wek")
        centralWek = Line.objects.get(title="Central", days="Wek")
        worcesWek = Line.objects.get(title="Worcester", days="Wek")
        capefltsWek = Line.objects.get(title="Cape Flats", days="Wek")


        inboundNorth = Direction.objects.filter(title="In").get(line=northWek)
        outboundNorth = Direction.objects.filter(title="On").get(line=northWek)

        inboundCentral = Direction.objects.filter(title="In").get(line=centralWek)
        outboundCentral = Direction.objects.filter(title="On").get(line=centralWek)

        df = pd.read_excel("static/sheets/Area_Central_directions.xlsx", engine='openpyxl', sheet_name="times")
        arrival_times = []
        '''
        if Train.Direction.Line == North and 
        '''
        trains_north_outbound = Train.objects.filter(direction_id=outboundCentral)
        all_north_stops = Stop.objects.filter(line=centralWek)

        cape_platform = None
        stopsInLine = df['column1']
        arrival_times.clear()
        
        # Delete all records
        # Arrival.objects.filter(
        #     train__direction_id=outboundCentral
        # ).all().delete()

        # '''important: DELETE DUPLICATES'''
        # for row in Arrival.objects.filter(Q(stop__line=centralWek)).reverse():
        #     if Arrival.objects.filter(Q(stop__line=centralWek) & Q(arrival_time=None) & Q(arrival_time=row.arrival_time) & Q(stop__title=row.stop.title) ).count() > 1:
        #         print(row)
        #         row.delete()
        

        """Populate Schedules"""
        # for column in df:
        #     # print(zip(df[column],df[column].index))
        #     if column == "column1":
        #         pass
        #     else:
        #         for aTime in df[column]:
        #             if type(aTime) == float:
        #                 pass
        #             elif ". " in str(aTime):
        #                 pass
        #             else:
                        
        #                 position = int(df[df[column] == aTime].index[0])
        #                 aTime = str(aTime).replace("'","")
        #                 train_number = str(df[column][1]).replace("'","")
        #                 stop_name = stopsInLine[position]
        #                 arrival_time = None
        #                 platform_number = None
                        
        #                 if ("CAPE TOWN" in stop_name) :
        #                     platform_number = cape_platform
        #                 if "PLATFORM" in stop_name:
        #                     platform_number = aTime
        #                     cape_platform = platform_number
        #                 if ":" in str(aTime):
        #                     if len(str(aTime)) > 5:
        #                         aTime = aTime.replace(aTime[0:11], "").replace(aTime[16:],"")
        #                         # print("FIXED -------------", aTime)
        #                     arrival_time = aTime
                        
        #                 if ("TRAIN NO." in stop_name) or "PLATFORM" in stop_name:
        #                     pass
        #                 else:
        #                     # print(train_number)
        #                     print(stop_name, arrival_time, train_number, platform_number)
        #                     train_object = trains_north_outbound.get(train_number=train_number)
        #                     stop_object = all_north_stops.get(title=stop_name)
        #                     arrival = Arrival(
        #                         stop=stop_object,
        #                         train=train_object,
        #                         arrival_time=arrival_time,
        #                         platform_number=platform_number
        #                     )
        #                     if not Arrival.objects.filter(stop=stop_object,train=train_object).exists():
        #                         arrival.save()
        #                     arrival_times.append(arrival)


                          
                # print(len(arrival_times))
                # print('adding to database.....') 
                
                # Arrival.objects.bulk_create(arrival_times)

                # Arrival.objects.filter(
                #     train__direction_id=outboundCentral
                # ).all().delete()

                # if column == "column10":
                #     break  
                # 