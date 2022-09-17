from multiprocessing.resource_sharer import stop
import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand, CommandError
from western_cape.models import Stop, Line, Arrival, Direction, Train

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

        arriveNorth = Arrival.objects.filter(train__direction_id__line=northWek).order_by('train', 'arrival_time')

        # print(arriveNorth)
        # print(arriveNorth.count())
        for arrival in arriveNorth:
            print(arrival)
        print()

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