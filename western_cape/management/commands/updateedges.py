from itertools import count
from os import sep
import pandas as pd
import numpy as np
import json
import datetime
from collections import defaultdict, deque

from django.core.management.base import BaseCommand, CommandError


from western_cape.models import Stop, Line, Arrival, Direction, Train, GraphEdge

class Command(BaseCommand):
    help = 'Update Timetables'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        df = pd.read_excel("static/sheets/edges.xlsx", engine='openpyxl', sheet_name="graph")

        # for index, row in df.iterrows():

        #     cost = int(row['minutes'])
        #     stops = row['edges'].split("|")
        #     stop_from = stops[0]
        #     stop_to = stops[1]

        #     # GraphEdge.objects.create(
        #     #     stop_from=stop_from,
        #     #     stop_to=stop_to,
        #     #     cost=cost
        #     # )
        #     print(stop_from, stop_to, cost, "------added!")
        