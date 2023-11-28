import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier

pd.set_option('display.max_columns', None)


current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "owndata_processed.csv"

# read csv
data = pd.read_csv(f_path + csv_filename, sep="\t", na_values="NaN")
data = data.drop(data[data.Label == "Unknown"].index)
data = data.drop(data[data.Duration > 20000].index)


# separate data into train and test data
data = data.drop(columns=["Date", "Time", "Src_IP_Addr", "Dst_IP_Addr", "Host_IP", "Rate", "Domain_Name", "Adblocker"])

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
clf = MLPClassifier(solver='sgd', alpha=1e-5, hidden_layer_sizes=(10, 2), random_state=1)

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







