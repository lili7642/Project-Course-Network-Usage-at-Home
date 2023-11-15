import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("pilot4.csv", sep="\t", index_col=0)

# data = data.drop(columns=["Duration"] == 0.0)
# data = data.drop(data[data.Duration < 60000].index)
# data = data.drop(data[data.Bytes > 1e6].index)
# print(data.head(100))
dataNew = data.drop(data[data["Src_IP_Addr"] == "192.168.8.177"].index)


groups = data.groupby('Src_IP_Addr')
for name, group in groups:
    plt.plot(group.Duration, group.Bytes, marker='o', linestyle='', markersize=12, label=name)
    # plt.plot(x="Duration", y="Bytes", kind="scatter", linestyle='', markersize=12, label=name)
data.plot(x="Duration", y="Bytes", kind="scatter")#, c="Src IP Addr", cmap='gray') 


data19 = data.drop(data[data["Date"] != "2023-10-19"].index)

print(data19.head())

# dataNew.plot(x="Duration", y="Bytes", kind="scatter")#, c="Src IP Addr", cmap='gray') 


# To show the plot
plt.show()

# print(data["Date"])