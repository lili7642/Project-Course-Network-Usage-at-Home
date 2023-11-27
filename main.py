import os
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


print("Hello World!")

## ================= READING DATA ====================================

current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
f_name = "owndataset.txt"

# import dataset as panda dataframe, skip last rows with text
df = pd.read_fwf(f_path + f_name, nrows=739)
# df = pd.read_csv(f_path + f_name, delimiter ="\t", header=0)

print(df.head())
# add option for viewing all column
pd.set_option('display.max_columns', None)

# remove column with "->"
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Split IP address and port to two columns
df[['Src_IP_Addr', 'Src_Port']] = df['Src IP Addr:Port'].str.split(':', n=1, expand=True)
df[['Dst_IP_Addr', 'Dst_Port']] = df['Dst IP Addr:Port'].str.split(':', n=1, expand=True)
"Drop old combined column"
df = df.drop(columns=["Src IP Addr:Port", "Dst IP Addr:Port"])#,"Flows"])
# Rename columns
df = df.rename(columns={"seen": "Time", "Date first": "Date"})
# print(df.head(415))

## ====================================================================

## ====================== CORRECTING BYTES ============================

def convert_bytes(value):
    multiplier = {'K': 1e3, 'M': 1e6, 'G': 1e9, 'T': 1e12, 'P': 1e15}

    # Split value into numerical part and prefix (if present)
    parts = value.split()
    num_part = float(parts[0])
    prefix = parts[1] if len(parts) > 1 else None

    # Check if a valid prefix is present
    if prefix and prefix in multiplier:
        return num_part * multiplier[prefix]
    elif num_part is not None:
        return num_part
    else:
        return float(value)

## ====================================================================

## ================ COVERT TIME TO SECOND AFTER 0 ===================== 
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

## ================ COVERT TIME TO SECOND AFTER 0 ===================== 

df_test = df.copy()

print("\nCreating new column...")
# create_seconds_column(df_test)

# print(df_test)

csv_file = "csv_markus_data.csv"
# df_test = df_test.sort_values(by=['Seconds'])
# df_test['Bytes'] = df_test['Bytes'].apply(convert_bytes)
# df_test['Packets'] = df_test['Packets'].apply(convert_bytes)

df_test.to_csv(f_path + csv_file, sep="\t", index = False)

data19 = df_test.drop(df_test[df_test["Date"] != "2023-10-19"].index)
data19 = data19.drop(data19[data19["Src_IP_Addr"] == "192.168.8.177"].index)

print(data19.head(20))

# groups = data19.groupby("Src_IP_Addr")

# for name, group in groups:
#     plt.plot(group.Seconds, group.Bytes, marker='o', linestyle='', markersize=6, label=name)

# plt.show()

## ========= IMPLEMENT AUTOMATED REVERSE DNS LOOKUP ===================


## ====================================================================