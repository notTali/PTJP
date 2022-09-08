import pandas as pd
import numpy as np
import Algorithm
# sheets_dict = pd.read_excel('Sourthern_Line_All_Stops.xlsx', sheet_name=None, engine='openpyxl')

# all_sheets = []
# for name, sheet in sheets_dict.items():
#     sheet['sheet'] = name
#     sheet = sheet.rename(columns=lambda x: x.split('\n')[-1])
#     all_sheets.append(sheet)

# full_table = pd.concat(all_sheets)
# full_table.reset_index(inplace=True, drop=True)

# print(full_table)
stops = np.array(Algorithm.allstops)
df = pd.read_excel("static/sheets/Sourthern_Line_All_Stops.xlsx", sheet_name = [2], engine='openpyxl')
n_trains = df[2].shape[1] - 1 # total number of trains

filter_criteria = (df[2]["Column1"].isin(stops)) | (df[2]["Column1"] == "TRAIN NO.")
df1 = df[2].loc[ filter_criteria, ["Column1", "Column2"]] #Return column 1 and 2 only
print(df1)
