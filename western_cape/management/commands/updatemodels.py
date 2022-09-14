import pandas as pd
import numpy as np
import json
import datetime
from collections import defaultdict, deque

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Update Timetables'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass