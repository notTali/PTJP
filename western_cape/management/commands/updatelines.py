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

        northStops = Stop.objects.filter(line=northWek)
        centralStops = Stop.objects.filter(line=centralWek)
        malmesburyStops = Stop.objects.filter(line=malmsWek)
        worcesterStops = Stop.objects.filter(line=worcesWek)
        capeflatsStops = Stop.objects.filter(line=capefltsWek)
        southStops = Stop.objects.filter(line=southWek)
        # print(centralStops)




        '''
        Updating directions!
        '''

        # Inbound
        # (object, created)=Direction.objects.get_or_create(
        #     title="In",
        #     line=centralWek
        # )
        # object.stops.set(centralStops)
        # # Outbound
        # (returnObj, created)=Direction.objects.get_or_create(
        #     title="On",
        #     line=centralWek
        # )
        # returnObj.stops.set(centralStops)

        # Malmesbury
        (object, created)=Direction.objects.get_or_create(
            title="In",
            line=malmsWek
        )
        object.stops.set(malmesburyStops)
        # Outbound
        (returnObj, created)=Direction.objects.get_or_create(
            title="On",
            line=malmsWek
        )
        returnObj.stops.set(malmesburyStops)

        # Worcester
        (object, created)=Direction.objects.get_or_create(
            title="In",
            line=worcesWek
        )
        object.stops.set(worcesterStops)
        # Outbound
        (returnObj, created)=Direction.objects.get_or_create(
            title="On",
            line=worcesWek
        )
        returnObj.stops.set(worcesterStops)


        # Cape flats
        (object, created)=Direction.objects.get_or_create(
            title="In",
            line=capefltsWek
        )
        object.stops.set(capeflatsStops)
        # Outbound
        (returnObj, created)=Direction.objects.get_or_create(
            title="On",
            line=capefltsWek
        )
        returnObj.stops.set(capeflatsStops)

        # South
        (object, created)=Direction.objects.get_or_create(
            title="In",
            line=southWek
        )
        object.stops.set(southStops)
        # Outbound
        (returnObj, created)=Direction.objects.get_or_create(
            title="On",
            line=southWek
        )
        returnObj.stops.set(southStops)

