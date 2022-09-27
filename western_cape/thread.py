import datetime
import threading
from django.db.models import Q
import json
from django.http import JsonResponse
from search.models import Result

# from search.views import getShortestPathData, getShortestPathTrains, minutesBetween
from . import models


array_r = [0,0,5]

'''Returns the number of minutes between start and end time'''
# EXAMPLE startime = "17:35"
def minutesBetween(start_time, end_time):
    start_time = str(start_time)
    if len(start_time) > 5:
        start_time = start_time.replace(start_time[0:11], "").replace(start_time[16:],"")

    (s_hr, s_min) = start_time.split(':') #s_hr, s_min : start minute and start hour
    (e_hr, e_min) = end_time.split(':') #e_hr, e_min : end minute and start hour
    # start and end time objects
    s_dt = datetime.timedelta(hours=int(s_hr), minutes=int(s_min))
    e_dt = datetime.timedelta(hours=int(e_hr), minutes=int(e_min))
    difference = e_dt - s_dt
    result = ""
    if "-" in str(difference):
        difference = "0:00:00"
    result = str(difference).split(":")
    # print(e_dt, " - ", e_dt," =  ",difference, result)
    r_hr = int(result[0])
    if r_hr > 0:
        return r_hr*60 + int(result[1])
    else:
        return int(result[1])

def getShortestPathTrains(route, start, start_time):
    trains = []
    qs = models.TrainStop.objects.all() #.order_by('only_stops_at__arrival_time')  
    # print(route)          
    for stop in route: 
        qs = qs.filter(stops=stop) #Check if all stops are contained in the stops field
    aTrain = list(qs)
    for st in aTrain:
        train_stops = st.only_stops_at.filter(
            Q(arrival_time__startswith=start_time) & Q(stop__title=start)
        )
        for ts in train_stops:
            trains.append(ts.train)
            # print(trains)
    # print(trains)
    return trains

def getShortestPathData(route, train):
    route_data = []
    for stop in route: 
        arr = models.Arrival.objects.filter(stop=stop,train=train)
        if arr.count() >=1:
            route_data.append(
                arr
            )
            # print(list(arr))
        else:
            pass
    return route_data


class SearchResultsThread(threading.Thread):
    def __init__(self, paths, src):
        self.paths = paths
        self.src = src
        threading.Thread.__init__(self)
    
    


    def run(self):
        try:
            
            # if YSTERPLAAT, MUTUAL, and THORNTON are in the shortest path, get trains that goes to MUTUAL and the ones that starts at Mutual.
            YSTERPLAAT = models.Stop.objects.get(title="YSTERPLAAT")
            MUTUAL = models.Stop.objects.get(title="MUTUAL")
            THORNTON = models.Stop.objects.get(title="THORNTON")

            possible_routes = []

            # Check for route type (direct/indirect)
            if YSTERPLAAT in self.paths and MUTUAL in self.paths and THORNTON in self.paths: # Route contains train interchanges
                # print("You have to switch trains change train")
                sub_list_left = self.paths[:self.paths.index(MUTUAL)+1] # get stops for the first train
                sub_list_right = self.paths[self.paths.index(MUTUAL):] # get stops for the next train
                # print(sub_list_left,"\n", sub_list_right)
                shortest_path_trainsLeft = getShortestPathTrains(sub_list_left, self.src, "")
                
                for train in shortest_path_trainsLeft:
                    data = getShortestPathData(sub_list_left, train)
                    time1 = data[len(data)-1][0].arrival_time
                    # print("NEXT TRAIN")
                    # Check the end time for left and start time for right.
                    shortest_path_trainsRight = getShortestPathTrains(sub_list_right,"MUTUAL", "")
                    for train1 in shortest_path_trainsRight:
                        data2 = getShortestPathData(sub_list_right, train1)
                        # print(data | data2)
                        # possible_routes.append( data2 )
                        
                        time2 = data2[0][0].arrival_time
                        if minutesBetween(time1, time2) > 1 and minutesBetween(time1, time2) < 5:
                            possible_routes.append(data + data2)
                            
                            # print(data + data2)
                            dataPdata = []
                            for d in (data + data2):
                                dataPdata.append(d[0])
                                print(d[0])
                            print(dataPdata)
                            Result.objects.create(
                                title=train1.train_number+train.train_number
                            ).result.set(list(dataPdata))
                            print(train1.train_number+train.train_number, "added.....")
                            # print(data[len(data)-1][0].train.train_number, time1,"|",data2[0][0].train.train_number , time2)
                    
            else:
                """No direct trains available"""
                shortest_path_trains = getShortestPathTrains(self.paths, self.src, "")
                # print(shortest_path_trains)
                # print(getShortestPathData(pathss, shortest_path_trains[0]))
                
                for train in shortest_path_trains:
                    data = getShortestPathData(self.paths, train)
                    # possible_routes.append(data)
                    # print(data)
                    # Result.objects.create(
                    #     result=JsonResponse(list(data + data2),  safe=False)
                    # )
            
        except Exception as e:
            print(e)



    