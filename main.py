import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import socket
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer


#================= Data preprocessing ======================#
# Import dataset as panda dataframe, skip last rows with text
data = pd.read_fwf("../Data/pilot3.txt")
data = data.iloc[:-4] #Removes the summary lines
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# Split IP address and port to two columns, and drops the old column
data[['Src IP Addr', 'Src Port']] = data['Src IP Addr:Port'].str.split(':', n=1, expand=True)
data[['Dst IP Addr', 'Dst Port']] = data['Dst IP Addr:Port'].str.split(':', n=1, expand=True)
#data[['Bytes', 'Flows']] = data['Bytes Flows'].str.split(' ', n=1, expand=True)
#data[['Duration', 'Proto']] = data['Duration Proto'].str.split(' ', n=1, expand=True)
#data = data.drop(columns=["Src IP Addr:Port", "Dst IP Addr:Port", "Bytes Flows", "Flows", 'Duration Proto'])
data = data.drop(columns=["Src IP Addr:Port", "Dst IP Addr:Port", "Flows"])
data = data.rename(columns={"seen": "Time", "Date first": "Date"})
data['Src Port'] = data['Src Port'].str.extract(r'(\d+)')
data['Src Port'] = pd.to_numeric(data['Src Port'], errors='coerce')
#print(data)

## Split IP address and port to two columns, and drops the old column (OLD)
# data[['Src IP Addr', 'Src Port']] = data['Src IP Addr:Port'].str.split(':', n=1, expand=True)
# data[['Dst IP Addr', 'Dst Port']] = data['Dst IP Addr:Port'].str.split(':', n=1, expand=True)
# data = data.drop(columns=["Src IP Addr:Port", "Dst IP Addr:Port","Flows"])
# data = data.rename(columns={"seen": "Time", "Date first": "Date"})

def convert_bytes(value):
    multipliers = {'K': 1000, 'M': 1000000, 'G': 1000000000}

    # Split the value into numerical part and prefix (if present)
    parts = value.split()
    num_part = float(parts[0]) #if parts[0].isdigit() else None
    prefix = parts[1] if len(parts) > 1 else None

    # Check if a valid prefix is present
    if prefix and prefix in multipliers:
        return num_part * multipliers[prefix]
    elif num_part is not None:
        # If no valid prefix is found but there is a numerical part, return it as is
        return num_part
    else:
        # If neither numerical part nor valid prefix is found, return the original value
        return float(value)

# Apply the conversion function to the 'Bytes' column
data['Bytes'] = data['Bytes'].apply(convert_bytes)

# Create column with global seconds
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

create_seconds_column(data)

# Orders the data by time in ascending order
data = data.sort_values(by='Seconds', ascending=True)

# Reset the index
data = data.reset_index(drop=True)

# Changes Duration column to float
data['Duration'] = data['Duration'].astype(float)

# Relation between duration and bytes
# data['Rate'] = data['Bytes']/data['Duration'].replace(0, pd.NaT)

# Find clients IP address
client = data['Src IP Addr'].value_counts().idxmax()

# Initialize 'Host IP'-column from 'Src Ip Addr'
data['Host IP'] = data['Src IP Addr']

# If the destination IP is not equal to the clients IP, adds it to 'Host IP'-column
for index, row in data.iterrows():
    if row['Dst IP Addr'] != client:
        data.at[index, 'Host IP'] = row['Dst IP Addr']

# Find all unique addresses
unique_ip = data['Host IP'].unique()

#===================================================================#


#============ Code for reverse DNS Lookup ============#

#data_DNS = pd.DataFrame(columns=['IP', 'Host'])

# data_DNS['IP']=unique_ip
# host = []
# i=0
# for ip in unique_ip:
#     try:
#         host_name = socket.gethostbyaddr(ip)[0]
#         host.append(host_name)
#     except socket.herror:
#         host.append(None)
    
#     if i % 100 == 0:
#         print(i)
#     i += 1
# data_DNS['Host'] = host
# data_DNS.to_csv('./host_names', index=False)
    
#print(data_DNS)
#==================================================#

#========== Code for grouping ==========#
# Initialize a 'Group' column with NaN values
# data['Group'] = float('nan')

# # Gives the flows happening close to each other the same group number
# group_counter = 0
# t = 0.5
# for i in range(len(data) - 1):
#     if data.iloc[i + 1]['Seconds'] - data.iloc[i]['Seconds'] <= t:
#         if data.iloc[i]['Seconds'] - data.iloc[i-1]['Seconds'] > t:# If this is a new grouping, increase group_counter by one
#             group_counter += 1
#         data.at[i + 1, 'Group'] = group_counter
#         data.at[i, 'Group'] = group_counter
#==================================================#

#================= Code for changing Protocol to variables======================#

# get the dummies and store it in a variable
dummies = pd.get_dummies(data.Proto).astype(int)
 
# Concatenate the dummies to original dataframe
data = pd.concat([data, dummies], axis='columns')

# drop the values
data = data.drop(['Proto', 'Src Port', "Dst Port"], axis='columns')
data = data.fillna(0)

#===============================================================================#

#=============== Code for changing host ports to features ====================#

# Finds clients IP and only saves the first 3 octets
client = unique_ip.split('.')
client = '.'.join(client[:3])

# Creates a column for non-client ports
data['Host Port'] = None

# Adds the non-client port to the new column by checking that the ports (Src & Dst) does not contain the client IP
for index, row in data.iterrows():
    if client not in row['Src IP Addr']:
        data.at[index, 'Host Port'] = row['Src Port']
    elif client not in row['Dst IP Addr']:
        data.at[index, 'Host Port'] = row['Dst Port'] 

# Checks all unique ports used
unique_port = data['Host Port'].unique()
unique_port = unique_port[unique_port != None]

# Adds the unique ports as columns and initiates all to False
data[unique_port] = 0

# Checks every host port and adds a True statement to the correct column
nr_port = len(unique_port)
for col in data.columns[-nr_port:]:
    data[col] = (data['Host Port'] == int(col)).astype(int)

#===============================================================================#

#========================== Machine Learning model ===============================#
# Removes outliers and data labled "Unknown"
data = data.drop(data[data.Label == "Unknown"].index)
data = data.drop(data[data.Duration > 20000].index)

#bag-words url:sen
vectorizer = CountVectorizer(binary=True)
X = vectorizer.fit_transform(data['Domain_Name'])

df_bow = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Identify columns with only numeric names
numeric_columns = df_bow.columns[df_bow.columns.str.isnumeric()]

# Drop columns with only numeric names
df_bow.drop(numeric_columns, axis=1, inplace=True)

# print(len(data.index))
# print(len(df_bow.index))

data.reset_index(drop=True, inplace=True)
df_bow.reset_index(drop=True, inplace=True)
data = pd.concat([data, df_bow], axis=1)
# data = data.drop('Domain_Name', axis=1)


# Drop the large labled data point
# data = data.drop(data[data.Label == "Netflix"].index)
# data = data.drop(data[data.Label == "Youtube"].index)
# data = data.drop(data[data.Label == "Facebook"].index)
# data = data.drop(data[data.Label == "YouTube"].index)
# data = data.drop(data[data.Label == "Gmail"].index)
# data = data.drop(data[data.Label == "Instagram"].index)
# data = data.drop(data[data.Label == "X"].index)
# data = data.drop(data[data.Label == "Outlook Mail"].index)
# data = data.drop(data[data.Label == "Steam Gaming"].index)
# data = data.drop(data[data.Label == "Reddit"].index)
# data = data.drop(data[data.Label == "SVT Play"].index)
# data = data.drop(data[data.Label == "Twitch TV"].index)
# data = data.drop(data[data.Label == "Google Drive"].index)
# data = data.drop(data[data.Label == "Prime video"].index)
# data = data.drop(data[data.Label == "Amazon shopping"].index)
# data = data.drop(data[data.Label == "Google Drive"].index)


# Normalize data

columns = ['Bytes', 'Duration', 'Packets']
for column in columns:
    data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min()) 



# Separate data into train and test data
col_drop = ["Date", "Time", "Src_IP_Addr", "Dst_IP_Addr", "Host_IP", "Rate", "Domain_Name", 'Label'] # Adblocker
msk = np.random.rand(len(data)) < 0.8
train = data[msk]
test = data[~msk]

# Creates training X- and Y-data
Xtrain = train.drop(columns=col_drop)
Ytrain = train["Label"]

# Creates test X- and Y-data
Xtest = test.drop(columns=col_drop)
Ytest = test["Label"]

# print(Xtest)
# print(train)
# print(np.size(train))
# print(np.size(test))

# NN-model using lbfgs 
n = data["Label"].value_counts()
print(n)

clf = MLPClassifier(solver='adam',alpha=1e-5, hidden_layer_sizes=(10,10,15), random_state=1)

model = clf.fit(Xtrain, Ytrain)

Yhat = model.predict(Xtest)

# print(Yhat)
# print(Ytest)

def accuracy(yhat,ytest):
    print(yhat)
    print(ytest)
    count = 0
    for ind, _ in enumerate(yhat):
        if yhat[ind] == ytest[ind]:
            count += 1
    
    print(count/len(ytest))


accuracy(Yhat,np.array(Ytest))
#==================================================================#