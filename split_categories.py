import os
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)


current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "owndata_labeled.csv"
new_csv = "owndata_processed.csv"

# read csv
data = pd.read_csv(f_path + csv_filename, sep=",", na_values="NaN")
# data2 = pd.read_csv(f_path + csv_hostnames, sep="\t", na_values="NaN", index_col= 0)

# data = data.drop(data["192.168.8" in data["Src_IP_Addr"]].index)
data = data[data["Src_IP_Addr"].str.contains("192.168.8") == False] 
# data = data.drop(data[data["Src_IP_Addr"] == "192.168.8.196"].index)

 
# get the dummies and store it in a variable
dummies = pd.get_dummies(data.Proto)
dummies2 = pd.get_dummies(data.Src_Port)
 
# Concatenate the dummies to original dataframe
data = pd.concat([data, dummies], axis='columns')
data = pd.concat([data, dummies2], axis='columns')

# drop the values
data.drop(['Proto', 'Src_Port'], axis='columns')
 
# print the dataframe
print(data)

data.to_csv(f_path + new_csv, sep="\t", index = False)
