from itertools import count
from os import sep
import pandas as pd
import numpy as np
import json
import datetime
import operator

from django.db.models import Q
from functools import reduce
from collections import defaultdict, deque

from django.core.management.base import BaseCommand, CommandError


from western_cape.models import Stop, Line, Arrival, Direction, Train, GraphEdge, TrainStop

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
        
        # '''Get timetable for the starting stop'''
        # arrivals = Arrival.objects.filter(
        #     stop__title="BELLVILLE A",
        #     arrival_time__startswith="08:0"
        # ).order_by(
        #     'arrival_time',
        #     'train__train_number'
        # )[:30]



        routes = [
            ['CAPE TOWN', 'ESPLANADE', 'YSTERPLAAT', 'KENTEMADE', 'CENTURY CITY', 'AKASIA PARK', 'MONTE VISTA', 'DE GRENDEL', 'AVONDALE', 'OOSTERZEE', 'BELLVILLE A'],

            ['CAPE TOWN', 'ESPLANADE', 'YSTERPLAAT', 'MUTUAL', 'LANGA', 'BONTEHEUWEL A', 'BONTEHEUWEL D', 'LAVISTOWN', 'BELHAR', 'UNIBELL', 'PENTECH', 'SAREPTA', 'BELLVILLE A'],

            ['CAPE TOWN', 'ESPLANADE', 'YSTERPLAAT', 'MUTUAL', 'THORNTON', 'GOODWOOD', 'VASCO', 'ELSIES RIVER', 'PAROW', 'TYGERBERG', 'BELLVILLE A'],

            ['CAPE TOWN', 'WOODSTOCK', 'SALT RIVER', 'KOEBERG RD', 'MAITLAND', 'NDABENI', 'PINELANDS', 'LANGA', 'BONTEHEUWEL A', 'BONTEHEUWEL D', 'LAVISTOWN', 'BELHAR', 'UNIBELL', 'PENTECH', 'SAREPTA', 'BELLVILLE A'],

            ['CAPE TOWN', 'WOODSTOCK', 'SALT RIVER', 'KOEBERG RD', 'MAITLAND', 'WOLTEMADE', 'MUTUAL', 'LANGA', 'BONTEHEUWEL A', 'BONTEHEUWEL D', 'LAVISTOWN', 'BELHAR', 'UNIBELL', 'PENTECH', 'SAREPTA', 'BELLVILLE A'],

            ['CAPE TOWN', 'WOODSTOCK', 'SALT RIVER', 'KOEBERG RD', 'MAITLAND', 'WOLTEMADE', 'MUTUAL', 'THORNTON', 'GOODWOOD', 'VASCO', 'ELSIES RIVER', 'PAROW', 'TYGERBERG', 'BELLVILLE A']
        ]

        ts = TrainStop.objects.all()
        # print(ts)
        # for i in ts.only_stops_at.all():
        #     print(i)

        
        edges = GraphEdge.objects.all()
        # for edge in edges:
        #     if edge.stop_from and edge.stop_to in 


        rt = ['CAPE TOWN', 'WOODSTOCK', 'SALT RIVER', 'KOEBERG RD', 'MAITLAND', 'WOLTEMADE', 'MUTUAL', 'THORNTON', 'GOODWOOD', 'VASCO', 'ELSIES RIVER', 'PAROW', 'TYGERBERG', 'BELLVILLE A']
        trains = Train.objects.filter(reduce(operator.and_, ( Q(direction_id__stops__title__contains=x) for x in ['CAPE TOWN', 'WOODSTOCK', 'SALT RIVER'] )))
        # print(trains)
        
        train_no = ""
        for stp in rt:
            arrivals = Arrival.objects.filter(
                stop__title=stp,
                arrival_time__startswith="",
            ).order_by(
                'arrival_time',
                'train__train_number',
                 'train__direction_id__line__title'
            )

        #     print(stp)
        #     for arr in arrivals:
        #         if stp==rt[0]:
        #             train_no=arr.train.train_number
        #         print(arr.train.train_number, arr.arrival_time, end="  ")
        #         print()
        #     print()

        # print("Use this train:", train_no)
        
        trainSTP = TrainStop.objects.filter(train_number='3201')
        # print(list(trainSTP[0].only_stops_at.all()))

        trns = TrainStop.objects.all().values_list("only_stops_at", flat=True)
        # print(trns)

        # first_train = arrivals[0].train.train_number
        # print("First train --->", first_train)
        # for arr in arrivals:
        #     # if arr.stop.interchange:
        #     #     print("True")
        #     print(arr.train.train_number, arr.arrival_time, arr.train.direction_id.line.title +" line")
        print(Stop.objects.all()[2].line.all().count())