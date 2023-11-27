import os
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

print("Hello World!")

## ================= READING DATA ====================================

current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
f_name = "pilot3.txt"

# import dataset as panda dataframe, skip last rows with text
df = pd.read_fwf(f_path + f_name, nrows=100426)
# add option for viewing all column
pd.set_option('display.max_columns', None)
# remove column with "->"
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Split IP address and port to two columns
df[['Src IP Addr', 'Src Port']] = df['Src IP Addr:Port'].str.split(':', n=1, expand=True)
df[['Dst IP Addr', 'Dst Port']] = df['Dst IP Addr:Port'].str.split(':', n=1, expand=True)
"Drop old combined column"
df = df.drop(columns=["Src IP Addr:Port", "Dst IP Addr:Port","Flows"])
# Rename columns
df = df.rename(columns={"seen": "Time", "Date first": "Date"})
# print(df.head(415))

## ====================================================================






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


df_test = df.copy()

print("\nCreating new column...")
create_seconds_column(df_test)

# print(df_test)

# csv_file = "pilot4.csv"

# df_test.to_csv(f_path + csv_file, sep="\t")

data19 = df_test.drop(df_test[df_test["Date"] != "2023-10-19"].index)
data19 = data19.drop(data19[data19["Src IP Addr"] == "192.168.8.177"].index)

print(data19.head(20))

# groups = data19.groupby("Src IP Addr")

# for name, group in groups:
#     plt.plot(group.Seconds, group.Bytes, marker='o', linestyle='', markersize=6, label=name)

# plt.show()

uniques = set(np.concatenate([df["Src IP Addr"].unique(), df["Dst IP Addr"].unique()]))
print(uniques)
csv_file_unique = "unique.txt"

with open(f_path + csv_file_unique, "w") as f:
    for value in list(uniques):
        f.write(str(value) + "\n")

## ========= IMPLEMENT AUTOMATED REVERSE DNS LOOKUP ===================


## ====================================================================