import pandas as pd
import numpy as np
import json
import datetime
from collections import defaultdict, deque

from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import Search


allstops = [
    "ABBOTSDALE","AKASIA PARK","ARTOIS","ATHLONE","AVONDALE","BELHAR","BELLVILLE","BELLVILLE A","BELLVILLE D","BLACKHEATH","BONTEHEUWEL","BOTHA","BRACKENFELL","BREE RIVER","CAPE TOWN","CENTURY CITY","CHAVONNES","CHRIS HANI","CLAREMONT","CRAWFORD","DAL JOSAFAT","DE GRENDEL","DIEPRIVIER","DU TOIT","EERSTE RIVER A","EERSTE RIVER D","EIKENFONTEIN","ELSIES RIVER","ESPLANADE","FALSE BAY","FAURE","FIRGROVE","FISANTKRAAL","FISH HOEK","GLENCAIRN","GOODWOOD","GOUDA","GOUDINI RD","HARFIELD RD","HAZENDAL","HEATHFIELD","HEIDEVELD","HERMON","HUGUENOT","KALBASKRAAL","KALK BAY","KAPTEINSKLIP","KENILWORTH","KENTEMADE","KHAYELITSHA","KLAPMUTS","KLIPHEUWEL","KOEBERG RD","KOELENHOF","KRAAIFONTEIN","KUILS RIVER","KUYASA","LAKESIDE","LANGA","LANSDOWNE","LAVISTOWN","LENTEGEUR","LYNEDOCH","MAITLAND","MALAN","MALMESBURY","MANDALAY","MBEKWENI","MELLISH","MELTONROSE","MIKPUNT","MITCHELLS PL.","MONTE VISTA","MOWBRAY","MUIZENBERG","MULDERSVLEI","MUTUAL","NDABENI","NETREG","NEWLANDS","NOLUNGILE","NONKQUBELA","NYANGA","OBSERVATORY","OOSTERZEE","OTTERY","PAARDENEILAND","PAARL","PAROW","PENTECH","PHILIPPI","PINELANDS","PLUMSTEAD","RETREAT","ROMANS RIVER","RONDEBOSCH","ROSEBANK","SALT RIVER","SAREPTA","SIMON`S TOWN","SOETENDAL","SOMERSET WEST","SOUTHFIELD","ST JAMES","STEENBERG","STELLENBOSCH","STEURHOF","STIKLAND","STOCK ROAD","STRAND","SUNNY COVE","THORNTON","TULBAGHWEG","TYGERBERG","UNIBELL","VAN DER STEL","VASCO","VLOTTENBURG","VOELVLEI","WELLINGTON","WETTON","WINTEVOGEL","WITTEBOME","WOLSELEY","WOLTEMADE","WOODSTOCK","WORCESTER","WYNBERG","YSTERPLAAT" 
]


pathStr = []
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
            print(pathStr)
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
    full_path = deque() # declaring deque
    _destination = paths[destination] 
    while _destination != origin: 
        full_path.appendleft(_destination) 
        _destination = paths[_destination] 
    full_path.appendleft(origin) 
    full_path.append(destination) 
    return visited[destination], list(full_path)


'''Returns the number of minutes between start and end time'''
# EXAMPLE startime = "17:35"
def minutesBetween(start_time, end_time):
    (s_hr, s_min) = start_time.split(':') #s_hr, s_min : start minute and start hour
    (e_hr, e_min) = end_time.split(':') #e_hr, e_min : end minute and start hour
    # start and end time objects
    s_dt = datetime.timedelta(hours=int(s_hr), minutes=int(s_min))
    e_dt = datetime.timedelta(hours=int(e_hr), minutes=int(e_min))
    difference = e_dt - s_dt
    result = str(difference).split(":")
    r_hr = int(result[0])
    if r_hr > 0:
        return r_hr*60 + int(result[1])
    else:
        return int(result[1])

# To be changed: take file name as parameter.
def getTrainData(filename):
    stops = np.array(allstops)
    df = pd.read_excel(filename, sheet_name = [2], engine='openpyxl')
    n_trains = df[2].shape[1] - 1 # total number of trains

    filter_criteria = (df[2]["Column1"].isin(stops)) | (df[2]["Column1"] == "TRAIN NO.")
    df1 = df[2].loc[ filter_criteria, ["Column1", "Column2"]] #Return column 1 and 2 only

    train_number = df1.loc[2, "Column2"]
  
    data_dict = dict(zip(df1["Column1"],df1["Column2"]))

    dict_array = []
    dict_array.append(data_dict)
    
    data_json = json.dumps(dict_array, indent=4)
    # print(data_json)
    return data_dict
      

# Create your views here.
def results(request):
    obj = Search.objects.all()[0]

    strt = obj.start_stop
    ens = obj.end_stop
    
    graph = Graph(len(allstops))
    for node in allstops:
        graph.add_node(node) 
    
    trainStops = getTrainData("static/sheets/Sourthern_Line_All_Stops.xlsx")
    
    for key, value in trainStops.items():
        # 
        if key != "TRAIN NO.":
           
            temp = list(trainStops)
            try:
                res = temp[temp.index(key) + 1]
            except (ValueError, IndexError):
                res = None
            
            if res is not None:
                # write algorithm to get the start + end time from the provided time, if no time use the time at the start of the DB (ONLY consider times at the inputted stop)
                # This will also determine which train is being used and the line.
                graph.add_edge(key, res, minutesBetween(trainStops[key],trainStops[res])) 
            else:
                pass
                # print("End of route!")
    
    print("Please enter your starting and ending stop: ")
    src = obj.start_stop #input("Start: " )
    # while src not in allstops:
    #     src = input("Invalid input! Please enter another stop: ")
    end = obj.end_stop # input("End: " )
    # while end not in allstops:
    #     end = input("Invalid input! Please enter another stop: ")
    
    g = Graph(len(allstops)) # 7 nodes

    for key, value in trainStops.items():
        if key != "TRAIN NO.":
            # check if there is another stop after the current one:
            temp = list(trainStops)
            try:
                res = temp[temp.index(key) + 1]
            except (ValueError, IndexError):
                res = None
            if res is not None:
                g.addEdge(allstops.index(key), allstops.index(res))
            else:
                pass
                # print("End of route!")

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
        
    # print("\n******************************************\n")
    paths = "These are the all unique paths from {} to {}:\n".format(startInStr,finishInStr)# in str
    g.printAllPaths(startInNum, finishInNum) # in num

    dist, pathss = shortest_path(graph, src, end)
    # print("\n******************************************\n")
    shortest = "The shortest path from {} to {} is {} minutes with the stops: {}".format(src,end,dist,pathss)

    print(obj.start_stop, obj.end_stop)
    context = {'obj':obj, 'paths':paths, 'shortest':shortest}
    return render(request, 'search-results.html', context)

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


