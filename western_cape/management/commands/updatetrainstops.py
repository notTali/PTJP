# updatetrainstops


import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand, CommandError
from western_cape.models import Stop, Line, Arrival, Direction, Train, TrainStop

class Command(BaseCommand):
    help = 'Update Line'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        trainstops = TrainStop.objects.all()
        for arrival in trainstops:
            print(arrival)
            for stp in arrival.only_stops_at.all():
                print(stp.stop.title)
            print()