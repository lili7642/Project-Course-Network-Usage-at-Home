import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

import torch
import torch.nn as nn
import torch.optim as optim


pd.set_option('display.max_columns', None)


current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "owndata_processed.csv"

# read csv
data = pd.read_csv(f_path + csv_filename, sep="\t", na_values="NaN")
# print(data)
data = data.drop(data[data.Label == "Unknown"].index)
data = data.drop(data[data.Duration > 20000].index)

#bag-worda url:sen
vectorizer = CountVectorizer(binary=True)
X = vectorizer.fit_transform(data['Domain Name'])

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



# separate data into train and test data
data = data.drop(columns=["Date", "Time", "Src IP Addr", "Dst IP Addr", "Host IP", "Rate", "Domain Name"]) # Adblocker
# print("NEW DATA:")
# print(data)

# LABEL INTO INTEGER 
n = data["Label"].value_counts()
print(n)
LABELS_DICT = {}
for i in range(len(n)):
    LABELS_DICT[n.index.tolist()[i]] = i
print()
print("LABELS AND CORRESPONDING NUMBER:")
for key,val in LABELS_DICT.items():
    print(f"{val}\t{key}")

def label2num(label):
    return(LABELS_DICT[label])
def num2label(num):
    return next((key for key, val in LABELS_DICT.items() if val == num), None)


# DATA
X = data.drop("Label", axis = 1).to_numpy()
Y = data["Label"].apply(label2num).to_numpy() #translate label to corresponding integer

# TRAIN TEST SPLIT
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.2, random_state=13)
 
# TO TENSOR
Xtrain = torch.tensor(Xtrain, dtype=torch.float32)
Ytrain = torch.tensor(Ytrain, dtype=torch.long)
Xtest = torch.tensor(Xtest, dtype=torch.float32)
Ytest = torch.tensor(Ytest, dtype=torch.long)

# NETWORK CLASS
class Net(nn.Module):
    def __init__(self, input_size, h1, h2, h3, h4, output_size):
        super(Net, self).__init__()
        dropoutrate = 0.5
        self.fc1 = nn.Linear(input_size, h1)
        self.relu1 = nn.ReLU()
        self.dropout1 = nn.Dropout(dropoutrate)

        self.fc2 = nn.Linear(h1, h2)
        self.relu2 = nn.ReLU()

        self.fc3 = nn.Linear(h2, h3)
        self.relu3 = nn.ReLU()
        self.dropout2 = nn.Dropout(dropoutrate)

        self.fc4 = nn.Linear(h3, h4)
        self.relu4 = nn.ReLU()

        self.fc5 = nn.Linear(h4, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.dropout1(x)

        x = self.fc2(x)
        x = self.relu2(x)

        x = self.fc3(x)
        x = self.relu3(x)
        x = self.dropout2(x)

        x = self.fc4(x)
        x = self.relu4(x)

        x = self.fc5(x)
        return x

# NETWORK LAYER SIZES
input_size = X.shape[1]
h1 = 128
h2 = 64
h3 = 32
h4 = 16
output_size = len(LABELS_DICT)

# CREATE NEURAL NETWORK MODEL
model = Net(input_size, h1, h2, h3, h4, output_size)

# LOSS & EVALUATION
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr = 0.001) #create optimizer


# TRAINING
num_epochs = 1000
for epoch in range(num_epochs):
    outputs = model(Xtrain) #Prediction
    loss = criterion(outputs, Ytrain) #Loss calculation

    optimizer.zero_grad() #reset optimizer gradient
    loss.backward() # bakåt ?
    optimizer.step() # uppdatera vikter

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')

# PRINT ACCURACY
with torch.no_grad():
    model.eval()
    outputs_test = model(Xtest)
    predicted_labels = torch.argmax(outputs_test, dim=1)
    acc = torch.sum(predicted_labels == Ytest).item() / len(Ytest)
    print(f"Test Accuracy: {acc}")







