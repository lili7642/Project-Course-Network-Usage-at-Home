import os
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
import re

print("\nHello World!")

## ================= READING DATA ====================================

current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
f_name = "owndata_processed.csv"

# import dataset as panda dataframe, skip last rows with text
df = pd.read_csv(f_path+f_name, delimiter=",")


## ====================================================================

domains = list(df["Domain Name"].dropna())
print("")
for i in range(10):
    print(domains[i])
print("")

def split_dom_name(domain_string):
    parts = re.split(r'[.-]', domain_string)
    # print(parts)
    return(parts)

split_dom_name(domains[0])

df["Domain Name"] = df["Domain Name"].apply(lambda x: split_dom_name(x) if pd.notna(x) else x)

print(df)

csv_file_tokanized = "tokanized_domains.csv"

df.to_csv(f_path+csv_file_tokanized)