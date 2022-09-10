import pandas as pd
import numpy as np
import Algorithm
import json
import datetime




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
    ##print(result)
    r_hr = int(result[0])

    if r_hr > 0:
        return r_hr*60 + int(result[1])
    else:
        return int(result[1])


def getTrainData():
    stops = np.array(Algorithm.allstops)
    df = pd.read_excel("static/sheets/Sourthern_Line_All_Stops.xlsx", sheet_name = [2], engine='openpyxl')
    n_trains = df[2].shape[1] - 1 # total number of trains

    filter_criteria = (df[2]["Column1"].isin(stops)) | (df[2]["Column1"] == "TRAIN NO.")
    df1 = df[2].loc[ filter_criteria, ["Column1", "Column2"]] #Return column 1 and 2 only
    #df1["Column1"].replace("TRAIN NO.", "STOPS")


    train_number = df1.loc[2, "Column2"]
    # print(df1)
    #print("Train Number:",train_number)


    data_dict = dict(zip(df1["Column1"],df1["Column2"]))

    dict_array = []
    dict_array.append(data_dict)
    # dict_array.append(data_dict)
    #data_dict = data_dict.update(test_dict)
    
    data_json = json.dumps(dict_array, indent=4)
    
    return data_dict
    





allstops = [
    "ABBOTSDALE","AKASIA PARK","ARTOIS","AVONDALE","BELHAR","BELLVILLE","BELLVILLE A","BELLVILLE D","BLACKHEATH","BONTEHEUWEL","BOTHA","BRACKENFELL","BREE RIVER","CAPE TOWN","CENTURY CITY","CHAVONNES","CHRIS HANI","CLAREMONT","CRAWFORD","DAL JOSAFAT","DE GRENDEL","DIEPRIVIER","DU TOIT","EERSTE RIVER A","EERSTE RIVER D","EIKENFONTEIN","ELSIES RIVER","ESPLANADE","FALSE BAY","FAURE","FIRGROVE","FISANTKRAAL","FISH HOEK","GLENCAIRN","GOODWOOD","GOUDA","GOUDINI RD","HARFIELD RD","HAZENDAL","HEATHFIELD","HEIDEVELD","HERMON","HUGUENOT","KALBASKRAAL","KALK BAY","KAPTEINSKLIP","KENILWORTH","KENTEMADE","KHAYELITSHA","KLAPMUTS","KLIPHEUWEL","KOEBERG RD","KOELENHOF","KRAAIFONTEIN","KUILS RIVER","KUYASA","LAKESIDE","LANGA","LANSDOWNE","LAVISTOWN","LENTEGEUR","LYNEDOCH","MAITLAND","MALAN","MALMESBURY","MANDALAY","MBEKWENI","MELLISH","MELTONROSE","MIKPUNT","MITCHELLS PL.","MONTE VISTA","MOWBRAY","MUIZENBERG","MULDERSVLEI","MUTUAL","NDABENI","NETREG","NEWLANDS","NOLUNGILE","NONKQUBELA","NYANGA","OBSERVATORY","OOSTERZEE","OTTERY","PAARDENEILAND","PAARL","PAROW","PENTECH","PHILIPPI","PINELANDS","PLUMSTEAD","RETREAT","ROMANS RIVER","RONDEBOSCH","ROSEBANK","SALT RIVER","SAREPTA","SIMON`S TOWN","SOETENDAL","SOMERSET WEST","SOUTHFIELD","ST JAMES","STEENBERG","STELLENBOSCH","STEURHOF","STIKLAND","STOCK ROAD","STRAND","SUNNY COVE","THORNTON","TULBAGHWEG","TYGERBERG","UNIBELL","VAN DER STEL","VASCO","VLOTTENBURG","VOELVLEI","WELLINGTON","WETTON","WINTEVOGEL","WITTEBOME","WOLSELEY","WOLTEMADE","WOODSTOCK","WORCESTER","WYNBERG","YSTERPLAAT" 
]

north_stops = ["CAPE TOWN","MAITLAND","SALT RIVER","KOEBERG RD",
"WOODSTOCK","WOLTEMADE","MUTUAL","THORNTON","GOODWOOD",
"VASCO","ELSIES RIVER","PAROW","TYGERBERG","ESPLANADE","YSTERPLAAT","KENTEMADE","CENTURY CITY","AKASIA PARK","MONTE VISTA","DE GRENDEL","AVONDALE","OOSTERZEE","BELLVILLE A" ]


north_stopsInNum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

allstopsNum = [] # an array of indices of all stops
for stop in allstops:
    allstopsNum.append(allstops.index(stop))


if __name__ == '__main__':
    graph = Algorithm.Graph(23)
    for node in north_stops:
        graph.add_node(node) 
    
    # Add Nodes
    # for i in range(23):

    
    #Train 3201
    graph.add_edge("CAPE TOWN", "WOODSTOCK", 3)
    graph.add_edge("WOODSTOCK", "SALT RIVER", 4)
    graph.add_edge("SALT RIVER", "KOEBERG RD", 2)
    graph.add_edge("KOEBERG RD", "MAITLAND", 3)
    graph.add_edge("MAITLAND", "WOLTEMADE", 3)
    graph.add_edge("WOLTEMADE", "MUTUAL", 2)
    graph.add_edge("MUTUAL", "THORNTON", 3)
    graph.add_edge("THORNTON", "GOODWOOD", 2)
    graph.add_edge("GOODWOOD", "VASCO", 3)
    graph.add_edge("VASCO", "ELSIES RIVER", 3)
    graph.add_edge("ELSIES RIVER", "PAROW", 3)
    graph.add_edge("PAROW", "TYGERBERG", 2)
    graph.add_edge("TYGERBERG", "BELLVILLE A", 4)

    # Train 2801
    graph.add_edge("CAPE TOWN", "ESPLANADE", 3)
    graph.add_edge("ESPLANADE", "YSTERPLAAT", 6)
    graph.add_edge("YSTERPLAAT", "KENTEMADE", 4)
    graph.add_edge("KENTEMADE", "CENTURY CITY", 3)
    graph.add_edge("CENTURY CITY", "AKASIA PARK", 3)
    graph.add_edge("AKASIA PARK", "MONTE VISTA", 3)
    graph.add_edge("MONTE VISTA", "DE GRENDEL", 4)
    graph.add_edge("DE GRENDEL", "AVONDALE", 2)
    graph.add_edge("AVONDALE", "OOSTERZEE", 3)
    graph.add_edge("OOSTERZEE", "BELLVILLE A", 2)
    
    trainStops = getTrainData()
    

    # Connect table results
    
    # print(trainStops, type(trainStops))
    # def getNextStop():

    for key, value in trainStops.items():
        # 
        if key != "TRAIN NO.":
            print(key, value)
            # check if there is another stop after the current one:
            temp = list(trainStops)
            try:
                res = temp[temp.index(key) + 1]
            except (ValueError, IndexError):
                res = None
            
            if res is not None:
                print("Next stop:",res, trainStops[res])
            else:
                print("End of route!")
            
    
    print(len(allstops))
    print("-------**************************************-------")
    print("Available stops: " , len(north_stops))
    print("Please enter your starting and ending stop: ")
    src = input("Start: " )
    while src not in north_stops:
        src = input("Invalid input! Please enter another stop: ")
    end = input("End: " )
    while end not in north_stops:
        end = input("Invalid input! Please enter another stop: ")
    
    g = Algorithm.Graph(23) # 7 nodes

    g.addEdge(0, 4) 
    g.addEdge(4, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 1) 
    g.addEdge(1, 5) 
    g.addEdge(5, 6) 
    g.addEdge(6, 7) 
    g.addEdge(7, 8)
    g.addEdge(8, 9)
    g.addEdge(9, 10) 
    g.addEdge(10, 11)
    g.addEdge(11, 12) 
    g.addEdge(12, 22)


    g.addEdge(0, 13) 
    g.addEdge(13, 14)
    g.addEdge(14, 15)
    g.addEdge(15, 16) 
    g.addEdge(16, 17) 
    g.addEdge(17, 18) 
    g.addEdge(18, 19) 
    g.addEdge(19, 20)
    g.addEdge(20, 21)
    g.addEdge(21, 22) 

    startInNum = 0
    startInStr = "null"
    finishInNum = 0
    finishInStr = "null"
    for i in range(len(north_stops)): 
        if src == north_stops[i]:
            startInNum = i
            startInStr = north_stops[i]
        if end == north_stops[i]:
            finishInNum = i
            finishInStr = north_stops[i]
        
    print("\n******************************************")
    print ("These are the all unique paths from {} to {}:\n".format(startInStr,finishInStr)) # in str
    g.printAllPaths(startInNum, finishInNum) # in num

    dist, pathss = Algorithm.shortest_path(graph, src, end)
    print("\n******************************************")
    print("The shortest path from {} to {} is {} minutes with the stops: {}".format(src,end,dist,pathss))
