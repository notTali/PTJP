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

    train_number = df1.loc[2, "Column2"]
  
    data_dict = dict(zip(df1["Column1"],df1["Column2"]))

    dict_array = []
    dict_array.append(data_dict)
    
    data_json = json.dumps(dict_array, indent=4)
    print(data_json)
    return data_dict
  
allstops = [
    "ABBOTSDALE","AKASIA PARK","ARTOIS","ATHLONE","AVONDALE","BELHAR","BELLVILLE","BELLVILLE A","BELLVILLE D","BLACKHEATH","BONTEHEUWEL","BOTHA","BRACKENFELL","BREE RIVER","CAPE TOWN","CENTURY CITY","CHAVONNES","CHRIS HANI","CLAREMONT","CRAWFORD","DAL JOSAFAT","DE GRENDEL","DIEPRIVIER","DU TOIT","EERSTE RIVER A","EERSTE RIVER D","EIKENFONTEIN","ELSIES RIVER","ESPLANADE","FALSE BAY","FAURE","FIRGROVE","FISANTKRAAL","FISH HOEK","GLENCAIRN","GOODWOOD","GOUDA","GOUDINI RD","HARFIELD RD","HAZENDAL","HEATHFIELD","HEIDEVELD","HERMON","HUGUENOT","KALBASKRAAL","KALK BAY","KAPTEINSKLIP","KENILWORTH","KENTEMADE","KHAYELITSHA","KLAPMUTS","KLIPHEUWEL","KOEBERG RD","KOELENHOF","KRAAIFONTEIN","KUILS RIVER","KUYASA","LAKESIDE","LANGA","LANSDOWNE","LAVISTOWN","LENTEGEUR","LYNEDOCH","MAITLAND","MALAN","MALMESBURY","MANDALAY","MBEKWENI","MELLISH","MELTONROSE","MIKPUNT","MITCHELLS PL.","MONTE VISTA","MOWBRAY","MUIZENBERG","MULDERSVLEI","MUTUAL","NDABENI","NETREG","NEWLANDS","NOLUNGILE","NONKQUBELA","NYANGA","OBSERVATORY","OOSTERZEE","OTTERY","PAARDENEILAND","PAARL","PAROW","PENTECH","PHILIPPI","PINELANDS","PLUMSTEAD","RETREAT","ROMANS RIVER","RONDEBOSCH","ROSEBANK","SALT RIVER","SAREPTA","SIMON`S TOWN","SOETENDAL","SOMERSET WEST","SOUTHFIELD","ST JAMES","STEENBERG","STELLENBOSCH","STEURHOF","STIKLAND","STOCK ROAD","STRAND","SUNNY COVE","THORNTON","TULBAGHWEG","TYGERBERG","UNIBELL","VAN DER STEL","VASCO","VLOTTENBURG","VOELVLEI","WELLINGTON","WETTON","WINTEVOGEL","WITTEBOME","WOLSELEY","WOLTEMADE","WOODSTOCK","WORCESTER","WYNBERG","YSTERPLAAT" 
]

allstopsNum = [] # an array of indices of all stops
for stop in allstops:
    allstopsNum.append(allstops.index(stop))
if __name__ == '__main__':
    graph = Algorithm.Graph(len(allstops))
    for node in allstops:
        graph.add_node(node) 
    
    trainStops = getTrainData()
    

    for key, value in trainStops.items():
        # 
        if key != "TRAIN NO.":
           
            temp = list(trainStops)
            try:
                res = temp[temp.index(key) + 1]
            except (ValueError, IndexError):
                res = None
            
            if res is not None:
                graph.add_edge(key, res, minutesBetween(trainStops[key],trainStops[res]))
            else:
                pass
                # print("End of route!")
    
    # print("-------**************************************-------")
    print("Please enter your starting and ending stop: ")
    src = input("Start: " )
    while src not in allstops:
        src = input("Invalid input! Please enter another stop: ")
    end = input("End: " )
    while end not in allstops:
        end = input("Invalid input! Please enter another stop: ")
    
    g = Algorithm.Graph(len(allstops)) # 7 nodes

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
        
    print("\n******************************************\n")
    print ("These are the all unique paths from {} to {}:\n".format(startInStr,finishInStr)) # in str
    g.printAllPaths(startInNum, finishInNum) # in num

    dist, pathss = Algorithm.shortest_path(graph, src, end)
    print("\n******************************************\n")
    print("The shortest path from {} to {} is {} minutes with the stops: {}".format(src,end,dist,pathss))
