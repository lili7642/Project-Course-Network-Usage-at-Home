import torch
import torch.nn as nn
import torch.optim as optim

# NETWORK CLASS
class Net(nn.Module):
    def __init__(self, input_size, h1, h2, h3, h4, h5, h6, output_size):
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

        self.fc5 = nn.Linear(h4, h5)
        self.relu5 = nn.ReLU()
        self.dropout3 = nn.Dropout(dropoutrate)

        self.fc6 = nn.Linear(h5, h6)
        self.relu6 = nn.ReLU()

        self.fc7 = nn.Linear(h6, output_size)

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
        x = self.relu5(x)
        x = self.dropout3(x)

        x = self.fc6(x)
        x = self.relu6(x)

        x = self.fc7(x)
        return x