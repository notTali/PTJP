import pandas as pd
import numpy as np
import Algorithm
import json


stops = np.array(Algorithm.allstops)
df = pd.read_excel("static/sheets/Sourthern_Line_All_Stops.xlsx", sheet_name = [2], engine='openpyxl')
n_trains = df[2].shape[1] - 1 # total number of trains

filter_criteria = (df[2]["Column1"].isin(stops)) | (df[2]["Column1"] == "TRAIN NO.")
df1 = df[2].loc[ filter_criteria, ["Column1", "Column2"]] #Return column 1 and 2 only
#df1["Column1"].replace("TRAIN NO.", "STOPS")


train_number = df1.loc[2, "Column2"]
print(df1)
print("Train Number:",train_number)


data_dict = dict(zip(df1["Column1"],df1["Column2"]))

test_dict = data_dict | data_dict
#data_dict = data_dict.update(test_dict)

data_json = json.dumps(data_dict, indent=4)
print(data_json)
print(test_dict)