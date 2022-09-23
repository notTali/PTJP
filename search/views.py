from turtle import title
import pandas as pd
import numpy as np
import json
import datetime
from collections import defaultdict, deque
from django.db.models import Count
from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import Search
from western_cape.models import GraphEdge, Stop, Line, Arrival, Direction, Train, TrainStop
from django.db.models import Q

# Stop names
allstops = list(Stop.objects.all())


pathStr = []

stop_arrival = []
routes = []
class Graph(object):
    def __init__(self,vertices):
        self.V= vertices 
        self.nodes = set() 
        self.edges = defaultdict(list) 
        self.graph = defaultdict(list)
        self.distances = {} 
    def add_node(self, value):
        self.nodes.add(value) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance 
    
    
    def printAllPathsUtil(self, u, d, visited1, path1):
        global allstops
        global pathStr
        visited1[u]= True 
        path1.append(u)  
        if u==d:
            pathStr =[]
            for i in path1:
                pathStr.append(allstops[i])
            # print(pathStr) #prints available paths
            routes.append(pathStr)
        else: 
            for i in self.graph[u]: 
                if visited1[i]==False: 
                    self.printAllPathsUtil(i, d, visited1, path1) 

        path1.pop() 
        visited1[u]= False
 
    def printAllPaths(self,s, d):
        visited1 =[False]*(self.V) 
        path1 = []
        self.printAllPathsUtil(s, d,visited1, path1)
        

def dijkstra(graph, initial):
    visited = {initial: 0} #dictionary
    path = {} # dictionary
    nodes = set(graph.nodes) # creates a set object
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited: 
                if min_node is None:
                    min_node = node 
                elif visited[node] < visited[min_node]: 
                    min_node = node                 
        if min_node is None:
            break
        nodes.remove(min_node) 
        current_weight = visited[min_node]  
        for edge in graph.edges[min_node]: 
            try:
                weight = current_weight + graph.distances[(min_node, edge)] 
            except:
                continue
            if edge not in visited or weight < visited[edge]: 
                visited[edge] = weight                        
                path[edge] = min_node                         
    return visited, path

def shortest_path(graph, origin, destination): 
    visited, paths = dijkstra(graph, origin) #calling function
    # print(paths)
    full_path = deque() # declaring deque
    _destination = paths[destination] 
    while _destination != origin: 
        # print(origin, _destination)
        
        full_path.appendleft(_destination) 
        _destination = paths[_destination] 
    full_path.appendleft(origin) 
    full_path.append(destination) 
    return visited[destination], list(full_path)


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

# Create your views here.
def results(request):
    obj = Search.objects.all()[0]
    edges = GraphEdge.objects.all()

    strtS = Stop.objects.get(title=obj.start_stop)
    endS = Stop.objects.get(title=obj.end_stop)

    graph = Graph(len(allstops))
    for node in allstops:
        graph.add_node(node) 
 
    for edge in edges:
        # print(edge.stop_from, edge.stop_to)
        # print(type(edge.stop_from), type(edge.stop_to))
        graph.add_edge( Stop.objects.get(title=edge.stop_from), Stop.objects.get(title=edge.stop_to), edge.cost)
    
    # print("Please enter your starting and ending stop: ")
    

    src =  strtS
    end = endS 
    
    g = Graph(len(allstops)) 

    for edge in edges:
        g.addEdge(allstops.index( Stop.objects.get(title=edge.stop_from) ), allstops.index( Stop.objects.get(title=edge.stop_to) ))

    startInNum = 0
    startInStr = "null"
    finishInNum = 0
    finishInStr = "null"
    for i in range(len(allstops)): 
        if src == allstops[i]:
            startInNum = i
            startInStr = allstops[i]
        if end == allstops[i]:
            finishInNum = i
            finishInStr = allstops[i]
    print("These are the all unique paths from {} to {}:\n".format(startInStr,finishInStr))# in str
    routes.clear()
    g.printAllPaths(startInNum, finishInNum) # in num
    
    dist, pathss = shortest_path(graph, src, end)
    shortest = "The shortest path from {} to {} is {} minutes with the stops: {}".format(src,end,dist,pathss)

    possible_trains = getTrains(routes, src, "")
    # print(possible_trains)
    possible_routes = []
    for train in possible_trains:
        data = getRouteData(routes, train)
        possible_routes.append(data)
        # data.clear()
        # print(data)
           
    context = {'obj':obj,'shortest':shortest, "routes":routes, "possible_routes":possible_routes}
    return render(request, 'search-results.html', context)

# Returns all the trains that goes to the destination stop starting at the departing stop (sorted by time)
def getTrains(routes, start, start_time):
    trains = []
    for route in routes:
        '''ADDD MORE TRAINSTOPS'''
        qs = TrainStop.objects.all()  
        # print(route)          
        for stop in route: 
            qs = qs.filter(stops=stop) #Check if all stops are contained in the stops field
        aTrain = list(qs)
        # print(aTrain)
        for st in aTrain:
            train_stops = st.only_stops_at.filter(
                Q(arrival_time__startswith=start_time) & Q(stop__title=start)
            )
            for ts in train_stops:
                trains.append(ts.train)
        print()
    return trains

def getRouteData(routes, train):
    route_data = dict()
    # print(train)
    for route in routes:
        # print(route)
        for stop in route: 
            # Only update if queryset.count() is > 1 
            arr = Arrival.objects.filter(stop=stop,train=train)

            if arr.count() >=1:
                route_data.update(
                    {stop.title: arr}
                )
            else:
                pass
        print()
    return route_data

def SearchPage(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        Search.objects.all().delete()
        if form.is_valid():
            form.save()
            return redirect(results)
    context = {'form':form}
    return render(request, 'search.html', context)

def getRoutes(start_stop, end_stop, starttime, endtime):
    
    southWek = Line.objects.get(title="Southern", days="Wek")
    northWek = Line.objects.get(title="Northern", days="Wek")
    malmsWek = Line.objects.get(title="Malmesbury", days="Wek")
    centralWek = Line.objects.get(title="Central", days="Wek")
    worcesWek = Line.objects.get(title="Worcester", days="Wek")
    capefltsWek = Line.objects.get(title="Cape Flats", days="Wek")


    inboundNorth = Direction.objects.filter(title="In").get(line=northWek)
    outboundNorth = Direction.objects.filter(title="On").get(line=northWek)

    arriveNorth = Arrival.objects.filter(train__direction_id__line=northWek).order_by('train__train_number', 'arrival_time')

    # print(arriveNorth)

    temp = Arrival.objects.filter(
        train__direction_id__line=northWek
    ).filter(
        # train__direction_id__stops__title__startswith="WOODSTOCK"
        Q(train__direction_id__stops__title__startswith=start_stop) & Q(train__direction_id__stops__title__startswith=end_stop)
        
    ).filter(
        # train__direction_id__stops__title__startswith="KRAAIFONTEIN"
    ).filter(
        arrival_time__startswith=starttime,
        # arrival_time__endswith=endtime
    ).order_by('train__train_number'
    ).values('train__train_number'
    ).annotate(count=Count('train__train_number'))

    routes = []
    for t in temp:
        vls = list(t.values())
        route = dict()
        trainStops = arriveNorth.filter(train__train_number=vls[0])
        for arrival in trainStops:
            route[arrival.stop.title] = str(arrival.arrival_time)
        routes.append(route)
    
    return routes[0]