import pandas as pd
import os
import socket
from timeout_decorator import timeout # pip install timeout_decorator

current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
f_name = "pilot3.txt"
csv_file = "pilot4.csv"
IP_hostName_file = "hostName.csv"

data = pd.read_csv(f_path + csv_file , sep="\t", index_col=0)
# Get unique values from a specific column
dataNew = data.drop(data[data["Src_IP_Addr"] == "192.168.8.177"].index)
unique_ip = dataNew['Src_IP_Addr'].unique()

# print(unique_ip)

# Convert the unique values to a list
unique_ip_list = list(unique_ip)
# print(unique_ip_list)

# @timeout(1)
def reverse_dns_lookup(ip_address):
    try:
        host_name, _, _ = socket.gethostbyaddr(ip_address)
        return host_name
    except socket.herror:
        return None

# Example usage
# ip_address = "115.167.7.199"
# host_name = reverse_dns_lookup(ip_address)

ip_host = {"IP_addr": [], "Host_name": []} 
length = len(unique_ip_list)

for index, ip in enumerate(unique_ip_list):
    # try:
    host_name = reverse_dns_lookup(ip)
    # except TimeoutError:
    #     ip_host["IP_addr"].append(ip)
    #     ip_host["Host_name"].append("NaN")
    if host_name:
        # print(f"Reverse DNS lookup for {ip}: {host_name}")
        ip_host["IP_addr"].append(ip)
        ip_host["Host_name"].append(host_name)
    else:
        # print(f"Reverse DNS lookup failed for {ip}")
        ip_host["IP_addr"].append(ip)
        ip_host["Host_name"].append("NaN")
    if index%100 == 0:
        print(f"{index}/{length}")

df = pd.DataFrame.from_dict(ip_host)

df.to_csv(f_path + IP_hostName_file, sep="\t")

