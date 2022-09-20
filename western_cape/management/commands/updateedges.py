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
        allstops = [
            "ABBOTSDALE","AKASIA PARK","ARTOIS","ATHLONE","AVONDALE","BELHAR","BELLVILLE","BELLVILLE A","BELLVILLE D","BLACKHEATH","BONTEHEUWEL","BOTHA","BRACKENFELL","BREE RIVER","CAPE TOWN","CENTURY CITY","CHAVONNES","CHRIS HANI","CLAREMONT","CRAWFORD","DAL JOSAFAT","DE GRENDEL","DIEPRIVIER","DU TOIT","EERSTE RIVER A","EERSTE RIVER D","EIKENFONTEIN","ELSIES RIVER","ESPLANADE","FALSE BAY","FAURE","FIRGROVE","FISANTKRAAL","FISH HOEK","GLENCAIRN","GOODWOOD","GOUDA","GOUDINI RD","HARFIELD RD","HAZENDAL","HEATHFIELD","HEIDEVELD","HERMON","HUGUENOT","KALBASKRAAL","KALK BAY","KAPTEINSKLIP","KENILWORTH","KENTEMADE","KHAYELITSHA","KLAPMUTS","KLIPHEUWEL","KOEBERG RD","KOELENHOF","KRAAIFONTEIN","KUILS RIVER","KUYASA","LAKESIDE","LANGA","LANSDOWNE","LAVISTOWN","LENTEGEUR","LYNEDOCH","MAITLAND","MALAN","MALMESBURY","MANDALAY","MBEKWENI","MELLISH","MELTONROSE","MIKPUNT","MITCHELLS PL.","MONTE VISTA","MOWBRAY","MUIZENBERG","MULDERSVLEI","MUTUAL","NDABENI","NETREG","NEWLANDS","NOLUNGILE","NONKQUBELA","NYANGA","OBSERVATORY","OOSTERZEE","OTTERY","PAARDENEILAND","PAARL","PAROW","PENTECH","PHILIPPI","PINELANDS","PLUMSTEAD","RETREAT","ROMANS RIVER","RONDEBOSCH","ROSEBANK","SALT RIVER","SAREPTA","SIMON`S TOWN","SOETENDAL","SOMERSET WEST","SOUTHFIELD","ST JAMES","STEENBERG","STELLENBOSCH","STEURHOF","STIKLAND","STOCK ROAD","STRAND","SUNNY COVE","THORNTON","TULBAGHWEG","TYGERBERG","UNIBELL","VAN DER STEL","VASCO","VLOTTENBURG","VOELVLEI","WELLINGTON","WETTON","WINTEVOGEL","WITTEBOME","WOLSELEY","WOLTEMADE","WOODSTOCK","WORCESTER","WYNBERG","YSTERPLAAT" 
        ]
        edg = GraphEdge.objects.all().values_list("stop_from", flat=True)
        ed1 = GraphEdge.objects.all().values_list("stop_from", flat=True)
        