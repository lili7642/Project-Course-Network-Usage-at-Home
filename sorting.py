import os
import pandas as pd
import matplotlib.pyplot as plt

## ================= READING DATA ====================================

current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "hostName.csv"

data = pd.read_csv(f_path + csv_filename, sep="\t", na_values="NaN")

print(data.head())
# data = data.sort_values(by=['IP_addr'])

data.to_csv(f_path + csv_filename, sep="\t", index = False, na_rep="NaN")
