import os
import pandas as pd
import matplotlib.pyplot as plt

## ================= READING DATA ====================================

current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "csv_data.csv"

data = pd.read_csv(f_path + csv_filename, sep="\t")

# data = data.drop(columns=["Duration"] == 0.0)
data = data.drop(data[data.Bytes > 60000].index)
# data = data.drop(data[data.Bytes > 1e6].index)
# print(data.head(100))
# dataNew = data.drop(data[data["Src_IP_Addr"] == "192.168.8.177"].index)


groups = data.groupby('Proto')
fig, ax = plt.subplots(figsize=(18,6))
for name, group in groups:
    plt.plot(group.Seconds, group.Bytes, marker='o', linestyle='', markersize=5, label=name)
    # group.plot(x="Seconds", y="Bytes", marker='o', kind="scatter",ax=ax, label=name)
# data.plot(x="Seconds", y="Bytes", kind="scatter")#, c="Src IP Addr", cmap='gray') 


# data19 = data.drop(data[data["Date"] != "2023-10-19"].index)

# print(data19.head())

# dataNew.plot(x="Duration", y="Bytes", kind="scatter")#, c="Src IP Addr", cmap='gray') 


# To show the plot
plt.legend()
plt.show()

# print(data["Date"])