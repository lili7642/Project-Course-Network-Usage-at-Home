import os
import pandas as pd


print("Hello World!")

## ================= READING DATA ====================================

import pandas as pd


# import dataset as panda dataframe, skip last rows with text
df = pd.read_fwf("pilot3.txt", nrows=100426) 

# add option for viewing all column
pd.set_option('display.max_columns', None)

# remove column with "->"
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Split IP address and port to two columns
df[['Src IP Addr', 'Src Port']] = df['Src IP Addr:Port'].str.split(':', n=1, expand=True)
df[['Dst IP Addr', 'Dst Port']] = df['Dst IP Addr:Port'].str.split(':', n=1, expand=True)

"Drop old combined column"
df = df.drop(columns=["Src IP Addr:Port", "Dst IP Addr:Port","Flows"])

"Rename columns"
df = df.rename(columns={"seen": "Time", "Date first": "Date"})

# Function to convert prefixes to actual quantities
def convert_bytes(value):
    multipliers = {'K': 1000, 'M': 1000000, 'G': 1000000000}

    # Split the value into numerical part and prefix (if present)
    parts = value.split()
    num_part = float(parts[0]) #if parts[0].isdigit() else None
    prefix = parts[1] if len(parts) > 1 else None
    # print(f"Numpart is {num_part} and prefix is {prefix}")

    # Check if a valid prefix is present
    if prefix and prefix in multipliers:
        # print(num_part*multipliers[prefix])
        return num_part * multipliers[prefix]
    elif num_part is not None:
        # If no valid prefix is found but there is a numerical part, return it as is
        return num_part
    else:
        # If neither numerical part nor valid prefix is found, return the original value
        return float(value)

# Apply the conversion function to the 'Bytes' column
df['Bytes'] = df['Bytes'].apply(convert_bytes)


print(df.head(415))

df.to_csv("pilot4.csv", sep= "\t")

## ====================================================================
 

## ========= IMPLEMENT AUTOMATED REVERSE DNS LOOKUP ===================


## ====================================================================
