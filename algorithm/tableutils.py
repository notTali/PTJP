import pandas as pd

# sheets_dict = pd.read_excel('Sourthern_Line_All_Stops.xlsx', sheet_name=None, engine='openpyxl')

# all_sheets = []
# for name, sheet in sheets_dict.items():
#     sheet['sheet'] = name
#     sheet = sheet.rename(columns=lambda x: x.split('\n')[-1])
#     all_sheets.append(sheet)

# full_table = pd.concat(all_sheets)
# full_table.reset_index(inplace=True, drop=True)

# print(full_table)
xlsx = pd.read_excel("static/sheets/Sourthern_Line_All_Stops.xlsx", sheet_name = [3], engine='openpyxl')
#sheet1 = xls.parse(0)

print(xlsx)