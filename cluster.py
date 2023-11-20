import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def convert_protocal(value):
    "function for conveerting protocal to numerical lables"
    protocal = {"ICMP": 1, "IGMP": 2, "UDP": 3, "TCP": 4}

    return protocal[value]


## ================= READING DATA ====================================

current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "csv_data.csv"

data = pd.read_csv(f_path + csv_filename, sep="\t")

# Remove large outliers from data
data = data.drop(data[data.Bytes > 60000].index)

# Remove columns before applying k-means clustering
data_cleaned = data.drop(columns=["Date", "Packets", "Seconds", "Time", "Src_IP_Addr", "Dst_IP_Addr"])
data_cleaned["Proto"] = data_cleaned["Proto"].apply(convert_protocal)
data_array = data_cleaned.to_numpy()
# print(data_array)
print(data_cleaned.head())

kmeans = KMeans(n_clusters=100, random_state=0, n_init="auto").fit(data_array)

print(kmeans.labels_)


# Insert lables into data 
data["lables"] = kmeans.labels_

# print result 
groups = data.groupby('lables')
fig, ax = plt.subplots(figsize=(18,6))
for name, group in groups:
    plt.plot(group.Seconds, group.Bytes, marker='o', linestyle='', markersize=5, label=name)

# To show the plot
plt.legend()
plt.show()