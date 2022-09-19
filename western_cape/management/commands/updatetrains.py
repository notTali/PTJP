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

        inboundCentral = Direction.objects.filter(title="In").get(line=centralWek)
        outboundCentral = Direction.objects.filter(title="On").get(line=centralWek)

        df = pd.read_excel("static/sheets/Area_North_directions.xlsx", engine='openpyxl', sheet_name=None)
        dfCentral = pd.read_excel("static/sheets/Area_Central_directions.xlsx", engine='openpyxl', sheet_name=None)
        northOutboundTrains = df["trains"]['TRAIN NO.'].values.tolist()
        centralOutboundTrains = dfCentral["trains"]['TRAIN NO.'].values.tolist()
        

        # North Outbound
        # for train_number in northOutboundTrains:
        #     Train.objects.create(
        #         train_number=train_number,
        #         direction_id=outboundNorth
        #     )
        #     print(train_number, ".............added!")

        # Train.objects.filter(
        #     direction_id=outboundCentral
        # ).delete()
        # Central outbound
        for train_number in centralOutboundTrains:
            Train.objects.create(
                train_number=train_number,
                direction_id=outboundCentral
            )
            print(train_number, ".............added!")
        