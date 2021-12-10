#!/usr/bin/python3#
#import random
import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
#acquisizione dati
pd.read_csv("DataSeq.csv")
#salvare i dati dentro una variabile
dataset = pd.read_csv("DataSeq.csv")
print ("*****************")
print(dataset.head())
print(dataset.shape)
print('***********')
#trasformazione dati n_cycle
print(dataset.columns)
all_data = dataset['n_cycle'].values.astype(float)
print(all_data)
#configurazione train data e test data
test_data_size = 10
train_data = all_data[:-test_data_size]
test_data = all_data[-test_data_size:]
print ('--- len train and test data ---')
print(len(train_data))
print(len(test_data))
print('-----test data ------')
print(test_data)
#normalizzazione dati
scaler = MinMaxScaler(feature_range=(-1, 1))
train_data_normalized = scaler.fit_transform(train_data .reshape(-1, 1))
print('--- stampa esempio dati normalizzati ---')
print(train_data_normalized[:5])
print(train_data_normalized[-5:])
# passaggio a tnsore per train data
train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)
print('-----torch.FloatTensor--------')
print (train_data_normalized)
print('---------------------')
# divisione tuple  di numeri
train_window = 10
# gestore di sequenza
def create_inout_sequences(input_data, tw):
    inout_seq = []
    L = len(input_data)
    for i in range(L-tw):
        train_seq = input_data[i:i+tw]
        train_label = input_data[i+tw:i+tw+1]
        inout_seq.append((train_seq ,train_label))
    return inout_seq
train_inout_seq = create_inout_sequences(train_data_normalized, train_window)
print('*** tuple di inout sequence esempio (2) *******')
print(train_inout_seq[:2])
print('*****************')
class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (torch.zeros(1,1,self.hidden_layer_size),
                            torch.zeros(1,1,self.hidden_layer_size))

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq) ,1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]

model = LSTM()
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
#------
print('----- modello ----')
print(model)
#-----------------------
# fase di addestramento
epochs = 100

for i in range(epochs):
    for seq, labels in train_inout_seq:
        optimizer.zero_grad()
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                        torch.zeros(1, 1, model.hidden_layer_size))

        y_pred = model(seq)

        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()

    if i%25 == 1:
        print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')
print ('°°°°°°°°°°°°°°°°°')
print(f'epoch: {i:3} loss: {single_loss.item():10.10f}')
print('°°°°°°°°°°°°°°°°°°°')
#--------------
fut_pred = 10

test_inputs = train_data_normalized[-train_window:].tolist()
print(test_inputs)
#-----------------------
model.eval()

for i in range(fut_pred):
    seq = torch.FloatTensor(test_inputs[-train_window:])
    with torch.no_grad():
        model.hidden = (torch.zeros(1, 1, model.hidden_layer_size),
                        torch.zeros(1, 1, model.hidden_layer_size))
        test_inputs.append(model(seq).item())
#------------
print('--- test input ---')
print(test_inputs[fut_pred:])
#--------------------
actual_predictions = scaler.inverse_transform(np.array(test_inputs[train_window:] ).reshape(-1, 1))
print ('***** ACTUAL PREDICTIONS')
print(actual_predictions)
x = np.arange (40, 50, 1)
# grafi dati 
#plt.title('sequences vs predictions')
#plt.ylabel('Total cycles')
#plt.grid(True)
#plt.autoscale(axis='x', tight=True)
#plt.plot(dataset['n_cycle'])
#plt.plot(x,actual_predictions)
#plt.savefig("Seq_predict.png")
#plt.show()
#-------vista particolare per previsione --------
plt.title('final sequences vs predictions')
plt.ylabel('final cycles')
plt.grid(True)
plt.autoscale(axis='x', tight=True)
plt.plot(dataset['n_cycle'][-train_window:])
plt.plot(x,actual_predictions)
#plt.scatter(actual_predictions,x, label="n_cycles", c='blue', marker='o', s=2)
#plt.legend()
plt.show()
