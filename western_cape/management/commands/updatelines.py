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
        # print(northStops)

        # Inbound
        (object, created)=Direction.objects.get_or_create(
            title="In",
            line=northWek
        )
        object.stops.set(northStops)
        # Outbound
        (returnObj, created)=Direction.objects.get_or_create(
            title="On",
            line=northWek
        )
        returnObj.stops.set(northStops)