from collections import defaultdict, deque
from enum import Enum



# class Type(Enum):
#     Normal = 1
#     Major = 2
#     EndOfRoute = 3
#     Interchange = 4

# class Stop:
#     def __init__(self, name, line):
#         self.name = name
#         self.line = line
#         # self.stop_type = stop_type # major, end of route, or rail interchange
    

# testStop = [
#     Stop("CAPE TOWN", "North")
# ]


allstops = [
    "ABBOTSDALE","AKASIA PARK","ARTOIS","ATHLONE","AVONDALE","BELHAR","BELLVILLE","BELLVILLE A","BELLVILLE D","BLACKHEATH","BONTEHEUWEL","BOTHA","BRACKENFELL","BREE RIVER","CAPE TOWN","CENTURY CITY","CHAVONNES","CHRIS HANI","CLAREMONT","CRAWFORD","DAL JOSAFAT","DE GRENDEL","DIEPRIVIER","DU TOIT","EERSTE RIVER A","EERSTE RIVER D","EIKENFONTEIN","ELSIES RIVER","ESPLANADE","FALSE BAY","FAURE","FIRGROVE","FISANTKRAAL","FISH HOEK","GLENCAIRN","GOODWOOD","GOUDA","GOUDINI RD","HARFIELD RD","HAZENDAL","HEATHFIELD","HEIDEVELD","HERMON","HUGUENOT","KALBASKRAAL","KALK BAY","KAPTEINSKLIP","KENILWORTH","KENTEMADE","KHAYELITSHA","KLAPMUTS","KLIPHEUWEL","KOEBERG RD","KOELENHOF","KRAAIFONTEIN","KUILS RIVER","KUYASA","LAKESIDE","LANGA","LANSDOWNE","LAVISTOWN","LENTEGEUR","LYNEDOCH","MAITLAND","MALAN","MALMESBURY","MANDALAY","MBEKWENI","MELLISH","MELTONROSE","MIKPUNT","MITCHELLS PL.","MONTE VISTA","MOWBRAY","MUIZENBERG","MULDERSVLEI","MUTUAL","NDABENI","NETREG","NEWLANDS","NOLUNGILE","NONKQUBELA","NYANGA","OBSERVATORY","OOSTERZEE","OTTERY","PAARDENEILAND","PAARL","PAROW","PENTECH","PHILIPPI","PINELANDS","PLUMSTEAD","RETREAT","ROMANS RIVER","RONDEBOSCH","ROSEBANK","SALT RIVER","SAREPTA","SIMON`S TOWN","SOETENDAL","SOMERSET WEST","SOUTHFIELD","ST JAMES","STEENBERG","STELLENBOSCH","STEURHOF","STIKLAND","STOCK ROAD","STRAND","SUNNY COVE","THORNTON","TULBAGHWEG","TYGERBERG","UNIBELL","VAN DER STEL","VASCO","VLOTTENBURG","VOELVLEI","WELLINGTON","WETTON","WINTEVOGEL","WITTEBOME","WOLSELEY","WOLTEMADE","WOODSTOCK","WORCESTER","WYNBERG","YSTERPLAAT" 
]

north_stops = ["CAPE TOWN","MAITLAND","SALT RIVER","KOEBERG RD",
"WOODSTOCK","WOLTEMADE","MUTUAL","THORNTON","GOODWOOD",
"VASCO","ELSIES RIVER","PAROW","TYGERBERG","ESPLANADE","YSTERPLAAT","KENTEMADE","CENTURY CITY","AKASIA PARK","MONTE VISTA","DE GRENDEL","AVONDALE","OOSTERZEE","BELLVILLE A" ]


north_stopsInNum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

allstopsNum = [] # an array of indices of all stops
for stop in allstops:
    allstopsNum.append(allstops.index(stop))


#print("All stops Num:", allstopsNum)

#cityInNum = [0,1,2,3,4,5,6]
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
        global north_stops
        global north_stopsInNum
        global pathStr
        visited1[u]= True 
        path1.append(u)  
  
        if u==d:
            pathStr =[]
            for i in path1:
                pathStr.append(north_stops[i])
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
#     print("path",path)
#     print("visited",visited)
    return visited, path


def shortest_path(graph, origin, destination): 
    visited, paths = dijkstra(graph, origin) #calling function
    full_path = deque() # declaring deque
    _destination = paths[destination] 
#     print("Paths[destination]",_destination)

    while _destination != origin: 
        full_path.appendleft(_destination) 
        _destination = paths[_destination] 

    full_path.appendleft(origin) 
    full_path.append(destination) 

    return visited[destination], list(full_path)

# if __name__ == '__main__':
#     graph = Graph(23)
#     for node in north_stops:
#         graph.add_node(node) 
#     #north_stops = ["CAPE TOWN","ESPLANADE","YSTERPLAAT","WOODSTOCK","SALT RIVER","KOEBERG RD","MAITLAND","WOLTEMADE","MUTUAL","THORNTON","GOODWOOD",
#     #"VASCO","ELSIES RIVER","PAROW","TYGERBERG","BELLVILLE A","BELLVILLE D" ]
    

#     # Need to add all trains in the Northern Line:
#     #Train 3201
#     graph.add_edge("CAPE TOWN", "WOODSTOCK", 3)
#     graph.add_edge("WOODSTOCK", "SALT RIVER", 4)
#     graph.add_edge("SALT RIVER", "KOEBERG RD", 2)
#     graph.add_edge("KOEBERG RD", "MAITLAND", 3)
#     graph.add_edge("MAITLAND", "WOLTEMADE", 3)
#     graph.add_edge("WOLTEMADE", "MUTUAL", 2)
#     graph.add_edge("MUTUAL", "THORNTON", 3)
#     graph.add_edge("THORNTON", "GOODWOOD", 2)
#     graph.add_edge("GOODWOOD", "VASCO", 3)
#     graph.add_edge("VASCO", "ELSIES RIVER", 3)
#     graph.add_edge("ELSIES RIVER", "PAROW", 3)
#     graph.add_edge("PAROW", "TYGERBERG", 2)
#     graph.add_edge("TYGERBERG", "BELLVILLE A", 4)

#     # Train 2801
#     graph.add_edge("CAPE TOWN", "ESPLANADE", 3)
#     graph.add_edge("ESPLANADE", "YSTERPLAAT", 6)
#     graph.add_edge("YSTERPLAAT", "KENTEMADE", 4)
#     graph.add_edge("KENTEMADE", "CENTURY CITY", 3)
#     graph.add_edge("CENTURY CITY", "AKASIA PARK", 3)
#     graph.add_edge("AKASIA PARK", "MONTE VISTA", 3)
#     graph.add_edge("MONTE VISTA", "DE GRENDEL", 4)
#     graph.add_edge("DE GRENDEL", "AVONDALE", 2)
#     graph.add_edge("AVONDALE", "OOSTERZEE", 3)
#     graph.add_edge("OOSTERZEE", "BELLVILLE A", 2)

#     print(len(allstops))
#     print("-------**************************************-------")
#     print("Available stops: " , len(north_stops))
#     print("Please enter your starting and ending stop: ")
#     src = input("Start: " )
#     while src not in north_stops:
#         src = input("Invalid input! Please enter another stop: ")
#     end = input("End: " )
#     while end not in north_stops:
#         end = input("Invalid input! Please enter another stop: ")
    
#     g = Graph(23) # 7 nodes

#     g.addEdge(0, 4) 
#     g.addEdge(4, 2)
#     g.addEdge(2, 3)
#     g.addEdge(3, 1) 
#     g.addEdge(1, 5) 
#     g.addEdge(5, 6) 
#     g.addEdge(6, 7) 
#     g.addEdge(7, 8)
#     g.addEdge(8, 9)
#     g.addEdge(9, 10) 
#     g.addEdge(10, 11)
#     g.addEdge(11, 12) 
#     g.addEdge(12, 22)


#     g.addEdge(0, 13) 
#     g.addEdge(13, 14)
#     g.addEdge(14, 15)
#     g.addEdge(15, 16) 
#     g.addEdge(16, 17) 
#     g.addEdge(17, 18) 
#     g.addEdge(18, 19) 
#     g.addEdge(19, 20)
#     g.addEdge(20, 21)
#     g.addEdge(21, 22) 

#     startInNum = 0
#     startInStr = "null"
#     finishInNum = 0
#     finishInStr = "null"
#     for i in north_stopsInNum: 
#         if src == north_stops[i]:
#             startInNum = north_stopsInNum[i]
#             startInStr = north_stops[i]
#         if end == north_stops[i]:
#             finishInNum = north_stopsInNum[i]
#             finishInStr = north_stops[i]
        
#     print("\n******************************************")
#     print ("These are the all unique paths from {} to {} :\n".format(startInStr,finishInStr)) # in str
#     g.printAllPaths(startInNum, finishInNum) # in num

#     dist, pathss = shortest_path(graph, src, end)
#     print("\n******************************************")
#     print("The shortest path from {} to {} is {} minutes with the paths : {}".format(src,end,dist,pathss))



