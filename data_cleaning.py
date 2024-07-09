import pandas as pd
import json
with open (r"D:\basel\GDP_ETL\columns.json","r") as file :
    initial_columns_data = json.load(file)
with open (r"D:\basel\GDP_ETL\rows.json","r") as file :
    rows_data = json.load(file)
with open (r"D:\basel\GDP_ETL\countries.json","r") as file :
    all_countries = json.load(file)
all_data={}
## filling missing values with the big indicator
def separate_categories(initial_columns_data):
    full_data = {}

    for country, values in initial_columns_data.items():
        temp_list = []
        j = 0
        for i in range(len(values)):
            if values[i] == "":
                temp_list.append(values[j:i])
                j = i + 1
        # Append the remaining part of values after the last empty string
        if j < len(values):
            temp_list.append(values[j:])
        
        full_data[country] = temp_list

    return full_data

def remove_empty_lists(data):
    for key, list_of_lists in data.items():
        data[key] = [lst for lst in list_of_lists if lst]
    return data

seperate_data =separate_categories(initial_columns_data)
cleaned_columns= remove_empty_lists(seperate_data)
cleaned_rows=remove_empty_lists(rows_data)
general_information_rows = [value[0] for value in cleaned_rows.values()]
general_information_columns = [value[0] for value in cleaned_columns.values()]

# df_general = pd.DataFrame(
#     [row[:-1] for row in general_information_rows], 
#     columns=general_information_columns[0]
#     )
# df_general.insert(0, 'country', all_countries[:len(general_information_rows)])
# df_general.to_csv('general_info_table.csv', index=False)
economic_indicators_rows = [value[1:2] for value in cleaned_rows.values()]
economic_indicators_columns = [value[1:2] for value in cleaned_columns.values()]
flattened_list_rows = [item for sublist in economic_indicators_rows for item in sublist]
flattened_list_columns = [item for sublist in economic_indicators_columns for item in sublist]
combined_list = [sublist[i:i+3] for sublist in flattened_list_rows for i in range(0, len(sublist), 3)]
df = pd.DataFrame(columns=flattened_list_columns)

print(df)