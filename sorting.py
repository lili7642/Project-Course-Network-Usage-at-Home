import os
import pandas as pd
import matplotlib.pyplot as plt
from ipwhois import IPWhois
import json


## ================= READING DATA ====================================

current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "csv_data.csv"
csv_hostnames = "hostName.csv"
data = pd.read_csv(f_path + csv_filename, sep="\t", na_values="NaN")
data2 = pd.read_csv(f_path + csv_hostnames, sep="\t", na_values="NaN", index_col= 0)



# obj = IPWhois('184.86.251.138')
# res2 = obj.lookup_whois()
# res = obj.lookup_rdap()
# print(json.dumps(res2,indent =2))

# print("-----------------------------")

# print(json.dumps(res,indent =2))
# temp = []

# for index, row in data2.iterrows():
#     # if data["Host_name"] == None:
#     if index % 100 == 0:
#         print("stage: ", index)
#     try:
#         obj = IPWhois(row["IP_addr"])
#         # print("Description: ",obj.lookup_whois()["nets"][0]["description"])
#         temp.append(obj.lookup_whois()["nets"][0]["description"])
#     except:
#         temp.append("NaN")
    # print(data)
    # res = obj.lookup_whois()["nets"][0]["description"]

# print(json.dumps(res,indent =2))
# print(data.head())
# data = data.sort_values(by=['IP_addr'])
# print(temp)

# csv_hostnamesNew = "hostNameDesc.csv"

# data2["Description"] = temp

# data2.to_csv(f_path + csv_hostnamesNew, sep="\t", index = False, na_rep="NaN")


# dataLonger = data.drop(data[data["Src IP Addr"] == 0].index)

# ## ================= Merge hostnames ====================================


merged_df = pd.merge(data, data2, left_on='Src_IP_Addr', right_on='IP_addr', how='left')

csv_data_with_hostname = "csv_data_wHostname.csv"
merged_df.to_csv(f_path + csv_data_with_hostname, sep="\t", index = False)


## ================= Group based on starting time ====================================

data = data.sort_values(by=['Seconds'])

# Gives the flows happening close to each other the same group number

group_counter = 0
t = 0.5
for i in range(len(data) - 1):
    if data.iloc[i + 1]['Seconds'] - data.iloc[i]['Seconds'] <= t:
        if data.iloc[i]['Seconds'] - data.iloc[i-1]['Seconds'] > t:# If this is a new grouping, increase group_counter by one
            group_counter += 1
        data.at[i + 1, 'Group'] = int(group_counter)
        data.at[i, 'Group'] = int(group_counter)

print(data)

csv_hostnamesNew = "data_wgroups.csv"

data.to_csv(f_path + csv_hostnamesNew, sep="\t", index = False, na_rep="NaN")