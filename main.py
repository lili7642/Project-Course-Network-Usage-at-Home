import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Import dataset as panda dataframe, skip last rows with text
data = pd.read_fwf("../Data/pilot3.txt")
data = data.iloc[:-4] #Removes the summary lines
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# Split IP address and port to two columns, and drops the old column
data[['Src IP Addr', 'Src Port']] = data['Src IP Addr:Port'].str.split(':', n=1, expand=True)
data[['Dst IP Addr', 'Dst Port']] = data['Dst IP Addr:Port'].str.split(':', n=1, expand=True)
data = data.drop(columns=["Src IP Addr:Port", "Dst IP Addr:Port","Flows"])
data = data.rename(columns={"seen": "Time", "Date first": "Date"})

def convert_bytes(value):
    multipliers = {'K': 1000, 'M': 1000000, 'G': 1000000000}

    # Split the value into numerical part and prefix (if present)
    parts = value.split()
    num_part = float(parts[0]) #if parts[0].isdigit() else None
    prefix = parts[1] if len(parts) > 1 else None

    # Check if a valid prefix is present
    if prefix and prefix in multipliers:
        return num_part * multipliers[prefix]
    elif num_part is not None:
        # If no valid prefix is found but there is a numerical part, return it as is
        return num_part
    else:
        # If neither numerical part nor valid prefix is found, return the original value
        return float(value)

# Apply the conversion function to the 'Bytes' column
data['Bytes'] = data['Bytes'].apply(convert_bytes)

# Create column with global seconds
def create_seconds_column(df):

    def create_datetime(date_str, time_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        time_obj = datetime.strptime(time_str, "%H:%M:%S.%f")
        datetime_obj = date_obj + timedelta(hours = time_obj.hour, minutes=time_obj.minute, seconds = time_obj.second, microseconds=time_obj.microsecond)
        return datetime_obj
    
    def seconds_diff(dt_obj, first_time):
        return((dt_obj-first_time).total_seconds())



    # first_time = create_datetime(df.iloc[0]["Date"], df.iloc[0]["Time"])
    first_time = min([create_datetime(date, time) for date,time in zip(df["Date"], df["Time"])])
    
    df["Seconds"] = df.apply(lambda row: seconds_diff(create_datetime(row["Date"], row["Time"]), first_time=first_time), axis = 1)

create_seconds_column(data)

# Orders the data by time in ascending order
data = data.sort_values(by='Seconds', ascending=True)

# Reset the index
data = data.reset_index(drop=True)

# Changes Duration column to float
data['Duration'] = data['Duration'].astype(float)
# Relation between duration and bytes
data['Rate'] = data['Bytes']/data['Duration'].replace(0, pd.NaT)

# Find clients IP address
client = data['Src IP Addr'].value_counts().idxmax()

# Initialize 'Host IP'-column from 'Src Ip Addr'
data['Host IP'] = data['Src IP Addr']

# If the destination IP is not equal to the clients IP, adds it to 'Host IP'-column
for index, row in data.iterrows():
    if row['Dst IP Addr'] != client:
        data.at[index, 'Host IP'] = row['Dst IP Addr']

# Initialize a 'Group' column with NaN values
data['Group'] = float('nan')

# Gives the flows happening close to each other the same group number
group_counter = 0
t = 0.5
for i in range(len(data) - 1):
    if data.iloc[i + 1]['Seconds'] - data.iloc[i]['Seconds'] <= t:
        if data.iloc[i]['Seconds'] - data.iloc[i-1]['Seconds'] > t:# If this is a new grouping, increase group_counter by one
            group_counter += 1
        data.at[i + 1, 'Group'] = group_counter
        data.at[i, 'Group'] = group_counter

# Reads host name
host_data = pd.read_csv('..\\hostName.csv', delimiter='\t')

# Merges the two dataframes to contain the correct Host name
data = pd.merge(data, host_data, left_on='Host IP', right_on='IP_addr', how='left')

# Drop unnecesary columns
data = data.drop(['IP_addr', 'Unnamed: 0'], axis=1)

print(data)


