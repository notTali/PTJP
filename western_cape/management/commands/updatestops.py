from itertools import count
from os import sep
import pandas as pd
import numpy as np
import json
import datetime
from collections import defaultdict, deque

from django.core.management.base import BaseCommand, CommandError

from search.views import getTrainData

from western_cape.models import Stop, Line, Arrival, Direction, Train

class Command(BaseCommand):
    help = 'Update Timetables'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
         
        southWek = Line.objects.get(title="Southern", days="Wek")
        northWek = Line.objects.get(title="Northern", days="Wek")
        malmsWek = Line.objects.get(title="Malmesbury", days="Wek")
        centralWek = Line.objects.get(title="Central", days="Wek")
        worcesWek = Line.objects.get(title="Worcester", days="Wek")
        capefltsWek = Line.objects.get(title="Cape Flats", days="Wek")


        

        df = pd.read_excel("static/sheets/Stops_per_Line.xlsx", engine='openpyxl')
        for column in df.columns:
            col_data = df[column]
            aLine=None
            if column == "Southern":
                aLine = southWek
            elif column == "Northern":
                aLine = northWek
            elif column == "Malmesbury":
                aLine = malmsWek
            elif column == "Central":
                aLine = centralWek
            elif column == "Worcester":
                aLine = worcesWek
            elif column == "Cape Flats":
                aLine = capefltsWek
            
            for row in range(len(col_data)):
                row_data = col_data[row]
                if type(row_data) != float:
                    Stop.objects.create(
                        title=row_data,
                    ).line.add(aLine)

                    print(row_data, column)
            print()