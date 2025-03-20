# input values (one-hot encoded):
#
# first 54 are each of the cards in the AI's hand 
# next 54 are the pseudo-randomly formed opponent's hand
# final 54 are the current move on the table
# order within each 54 follows that in deck.py

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


model = nn.Sequential(
    nn.Linear(162, 256),
    nn.ReLU(),
    nn.Linear(256, 256),
    nn.ReLU(),
    nn.Linear(256, 54),
    nn.Sigmoid()
)
print(model)

# https://machinelearningmastery.com/develop-your-first-neural-network-with-pytorch-step-by-step/
 
# train the model
loss_fn   = nn.BCELoss()  # binary cross entropy
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Simply speaking, the entire dataset is split into batches, and you pass the batches one by one into a model using a training loop. 
# Once you have exhausted all the batches, you have finished one epoch. 
# Then you can start over again with the same dataset and start the second epoch, continuing to refine the model. 
# This process repeats until you are satisfied with the model’s output.

 
n_epochs = 100
batch_size = 10
 
for epoch in range(n_epochs):
    for i in range(0, len(X), batch_size):
        Xbatch = X[i:i+batch_size]
        y_pred = model(Xbatch)
        ybatch = y[i:i+batch_size]
        loss = loss_fn(y_pred, ybatch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f'Finished epoch {epoch}, latest loss {loss}')
 
# compute accuracy (no_grad is optional)
with torch.no_grad():
    y_pred = model(X)
accuracy = (y_pred.round() == y).float().mean()
print(f"Accuracy {accuracy}")
