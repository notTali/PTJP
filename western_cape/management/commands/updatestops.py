import pandas as pd
import numpy as np
import json
import datetime
from collections import defaultdict, deque

from django.core.management.base import BaseCommand, CommandError

from search.views import getTrainData

class Command(BaseCommand):
    help = 'Update Timetables'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_excel("static/sheets/Stops_per_Line.xlsx", engine='openpyxl')
        print(df['North'])

    # def getTrainData():
        
    #     df = pd.read_excel("static/sheets/Stops_per_Line.xlsx", sheet_name = [1], engine='openpyxl')
    #     # n_trains = df[2].shape[1] - 1 # total number of trains

    #     # filter_criteria = (df[2]["Column1"].isin(stops)) | (df[2]["Column1"] == "TRAIN NO.")
    #     # df1 = df[2].loc[ filter_criteria, ["Column1", "Column2"]] #Return column 1 and 2 only

    #     # train_number = df1.loc[2, "Column2"]
    
    #     # data_dict = dict(zip(df1["Column1"],df1["Column2"]))

    #     # dict_array = []
    #     # dict_array.append(data_dict)
        
    #     # data_json = json.dumps(dict_array, indent=4)
    #     # print(data_json)
    #     return df