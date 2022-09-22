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
        # for arrival in trainstops:
        #     print(arrival)
        #     tstop = []
        #     for stp in arrival.only_stops_at.all():
        #         tstop.append(stp.stop)
        #     TrainStop.objects.get(
        #         train_number=arrival.train_number
        #     ).stops.set(tstop)
        #     print(arrival.train_number, "Added ....................")    
        