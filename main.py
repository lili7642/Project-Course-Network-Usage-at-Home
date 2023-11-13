import os
import pandas as pd


print("Hello World!")

## ================= READING DATA ====================================

current_directory = os.path.dirname(__file__)
f_path = current_directory+"/../../project_course_data/pilot3.txt"

# import dataset as panda dataframe, skip last rows with text
df = pd.read_fwf(f_path, nrows=100426)
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
print(df.head(415))

## ====================================================================
 

## ========= IMPLEMENT AUTOMATED REVERSE DNS LOOKUP ===================


## ====================================================================