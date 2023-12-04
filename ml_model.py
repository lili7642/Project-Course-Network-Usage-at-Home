import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer


pd.set_option('display.max_columns', None)


current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "owndata_processed.csv"

# read csv
data = pd.read_csv(f_path + csv_filename, sep="\t", na_values="NaN")
data = data.drop(data[data.Label == "Unknown"].index)
data = data.drop(data[data.Duration > 20000].index)

#bag-worda url:sen
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



# separate data into train and test data
data = data.drop(columns=["Date", "Time", "Src_IP_Addr", "Dst_IP_Addr", "Host_IP", "Rate", "Domain_Name"]) # Adblocker

msk = np.random.rand(len(data)) < 0.8
train = data[msk]
test = data[~msk]

Xtrain = train.drop(columns=["Label"])
Xtest = test.drop(columns=["Label"])

Ytrain = train["Label"]
Ytest = test["Label"]

# print(Xtest)


# print(train)

# print(np.size(train))
# print(np.size(test))

# # nn model using lbfgs 
n = data["Label"].value_counts()
print(n)

clf = MLPClassifier(solver='adam',alpha=1e-5, hidden_layer_sizes=(15,15), random_state=1)

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







